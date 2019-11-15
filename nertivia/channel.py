import requests 
import json
import asyncio
from nertivia.message import *

URL = "https://supertiger.tk/api/messages/channels/"
URL_MSG = "https://supertiger.tk/api/messages/"
URL_STA = "https://supertiger.tk/api/settings/status"







class Channel(object):
    def __init__(self, channel):
        self._channel = channel
        with open('constants.txt') as json_file:
            data = json.load(json_file)
            for p in data['constants']:
                self.token = p['token']

        self.headers = {'Accept': 'text/plain',
                'authorization': self.token,
                'Content-Type': 'application/json;charset=utf-8'}

    def send(self, message):
        data = {'message': message,
                'tempID': 0}  
        r = requests.post(url=str(URL + str(self._channel)), headers=self.headers, data=json.dumps(data))
    
    def get_message(self, messageID):
        sid = Message.testRequest(self=self, channel=self._channel)
        sid = sid.split('connect.sid=', 1)[1].strip('; Path=/; HttpOnly')
        headers1 = {'Accept': 'text/plain',
                    'authorization': self.token,
                    'Content-Type': 'application/json;charset=utf-8',
                    'Cookie': f'connect.sid={sid}' } 
        r = requests.get(url=str(f'https://supertiger.tk/api/messages/channels/{self._channel}?continue={messageID}'), headers=headers1)
        print(r.json())
        #mes = list(filter(lambda x: x['messageID'] == messageID, r.json()['messages']))
        message = Message(r.json())
        return message
      