import requests
import json
from urllib.request import Request, urlopen
import sys
import os 

if len(sys.argv) != 2:
    print('You have no or too many arguments given! >:c')
    sys.exit()

def nitro_checker_message_length(message):
    if len(message) > 2000 & nitro == 'none' or 'basic':
        print('Message too long! Max length for non nitro / nitro basic users is 2000 characters, you have', len(message), 'characters')
        sys.exit()
    elif len(message) > 4000:
        print('Message too long! Max length for Discord messages is 4000 characters, you have', len(message), 'characters')
        sys.exit()

def nitro_checker_file_size(file_name):
    file_size = os.path.getsize(file_name)
    file_size = file_size / 1000000
    if nitro == 'nitro':
        max_size = 500
        if file_size > max_size:
            print(f'File too big! Max size for nitro users is {max_size}MB, you have {file_size}MB')
            sys.exit()
    elif nitro == 'basic':
        max_size = 50
        if file_size > max_size:
            print(f'File too big! Max size for basic nitro users is {max_size}MB, you have {file_size}MB')
            sys.exit()
    elif nitro == 'none':
        max_size = 8
        if file_size > max_size:
            print(f'File too big! Max size for non nitro users is {max_size}MB, you have {file_size}MB')
            sys.exit()
    else:
        print('Nitro variable not set correctly! (can be "nitro", "basic" or "none"')
        sys.exit()

nitro = 'none' # default value = none: can be 'basic' for nitro basic or 'nitro' for normal nitro
file_name = sys.argv[1]
nitro_checker_file_size(file_name)
token = '' # your personal discord token
friends = []
friend = str(input('Type the name of a friend: ')) 
friend = friend.lower().strip()
message = str(input('Type a message (press enter for none): '))
nitro_checker_message_length(message)
found_friend = False

header = {
    'authorization': token,
}

files = {
    "file" : (f"./{file_name}", open(f"./{file_name}", 'rb')) 
}

payload = {
    "content": [message if message else '']
}

    
def get_headers(token=None, content_type='application/json'):
    headers = {
        'Content-Type': content_type,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }
    if token:
        headers.update({'Authorization': token})
    return headers

def get_chat(token, uid):
    try:
        return json.loads(urlopen(Request('https://discordapp.com/api/v6/users/@me/channels', headers=get_headers(token), data=json.dumps({'recipient_id': uid}).encode())).read().decode())['id']
    except:
        pass
    
def get_friends(token):
    try:
        return json.loads(urlopen(Request('https://discordapp.com/api/v6/users/@me/relationships', headers=get_headers(token))).read().decode())
    except:
        pass

data = get_friends(token)

for i in data:
    f = i['user']['username'], i['id']
    friends.append(f)

for i in friends:
    if friend == i[0].lower().strip():
        chat_id = get_chat(token, i[1])
        r = requests.post(f"https://discord.com/api/v9/channels/{chat_id}/messages", data=payload, headers=header, files=files)
        found_friend = True
        break

if not found_friend:
    print('Friend not found')
        

