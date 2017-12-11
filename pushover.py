# author: mpekalski@gmail.com

import requests

def pushover(message, config=None):
    # if you do not pass dictionary with pushover config 
    # it will try to read it from the file
    if not config:
        with open('pushover.config','r') as f:
            config = eval(f.read())
    url = 'https://api.pushover.net/1/messages.json'
    payload = {
     "token":   config['token'], 
     "user":    config['user'],  
     "message": message, 
     "device":  config['device']
    }
    headers={'Content-Type': 'application/json',  "User-Agent": "curl/7.47.0", "Accept": "*/*"}
    res = requests.post(url, json=payload, headers=headers)
    if res.status_code != 200:
        print("pushover, we've got a problem {}".format(res.status_code))
