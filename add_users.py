from telethon.sync import TelegramClient
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError, UserNotMutualContactError
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from dotenv import load_dotenv
import random
import time
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
    print('The following code which you should provide is not stored anywhere but your own computer.')
    print('Feel free to delete the .session file after you are done using this code.')
    print('You can check how this code is secured looking at the Telethon package')
    client.sign_in(phone, input('Enter the code: '))

GROUP_ID = int(os.getenv('GROUP_ID'))
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))
CHANNEL = client.get_entity('https://t.me/BrainTradingChannelBeta')
USERS_FILENAME = os.getenv('USERS_FILENAME')

ADD_TO_GROUP = os.getenv('ADD_TO_GROUP') == 'True'
ADD_TO_CHANNEL = os.getenv('ADD_TO_CHANNEL') == 'True'

if ADD_TO_GROUP or ADD_TO_CHANNEL:
    with open(USERS_FILENAME, 'r') as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader)

        for raw_user in reader:
            user = client.get_entity(PeerUser(int(raw_user[1])))
            print(f"Attempting to add #{user.id} - {user.username}")

            # Adding to a group
            if ADD_TO_GROUP:
                try:
                    client(AddChatUserRequest(GROUP_ID, user.id, fwd_limit=10))
                except UserAlreadyParticipantError:
                    print(f"User {user.username} is already a group participant")
                else:
                    print(f"User {user.username} successfully added to the group")

            # Adding to a SuperGroup/Channel
            if ADD_TO_CHANNEL:
                try:            
                    client(InviteToChannelRequest(CHANNEL, [user.id]))
                except UserNotMutualContactError:
                    print(f"User {user.username} is not a mutual contact")
                except UserAlreadyParticipantError:
                    print(f"User {user.username} is already a channel/supergroup participant")
                else:
                    print(f"User {user.username} successfully added to the channel")

            # Sleep between 30 and 50 seconds
            sleep_time = 40 + random.randint(-10, 11)
            print(f"Sleeping for {sleep_time} seconds")
            time.sleep(sleep_time)    


