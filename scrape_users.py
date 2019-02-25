from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.errors.rpcerrorlist import ChannelPrivateError
import csv
from dotenv import load_dotenv
import os
import csv
 
load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone = os.getenv('PHONE')
client = TelegramClient(phone, api_id, api_hash)
 
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))
 
chats = client(GetDialogsRequest(
             offset_date=None,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=200,
             hash = 0
         )).chats

groups = []
for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
    except:
        continue
 
print('Collecting members...')
for index in range(len(groups)):
    target_group = groups[index]

    print(f"Fetching participants from {target_group.title}")
    try:
        all_participants = client.get_participants(target_group, aggressive=True)
        
        filename = f"members_{'_'.join(target_group.title.lower().split(' '))}.csv"
        print(f"Saving to file {filename}...")
        with open('csv/' + filename,"w",encoding='UTF-8') as f:
            writer = csv.writer(f,delimiter=",",lineterminator="\n")
            writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
            for user in all_participants:
                username = user.username or ""
                first_name = user.first_name or ""
                last_name = user.last_name or ""
                name = (f"{first_name} {last_name}").strip()

                writer.writerow([username, user.id, user.access_hash, name, target_group.title, target_group.id])
    except ChannelPrivateError:
        print(f"ChannelPrivateError caught for {target_group.title} - Ignored")
              
print('Members collected successfully!')    