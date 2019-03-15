# Telegram Users Scraper

This code has a intention to provide a script to fetch all the users from all the code runner groups, to create a big dataset of members which might be interestend in a common thing, as well as provide an easy way to add this users to a group or a channel (with some restrictions imposed by Telegram)

# Usage

First, you must create your application following [this](https://core.telegram.org/api/obtaining_api_id) tutorial.

You must create a .env file in your root page, in the following format:

```env
API_ID=xxxxxx                               # You can get this as explained before
API_HASH='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # You can also get this as explained before
PHONE='+xxxxxxxxxxxxx'                      # Your telephone in the international format
GROUP_ID=111111111                          # ID of the group you want to add users
CHANNEL_ID=11111111111                      # ID of the channel or supergroup you want to add users
PASSWORD='xxxxxxx'                          # Telegram phone number password (required if 2FA is up)
USERS_FILENAME='csv/members_group_name.csv' # CSV generated by add_users.py
ADD_TO_GROUP='True'                         # If equals 'True', will add the users to GROUP_ID
ADD_TO_CHANNEL='True'                       # If equals 'True', will add the users to CHANNEL_ID
```
