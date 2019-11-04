import requests 
import json
import asyncio
import abc
from nertivia.message import *

URL = "https://supertiger.tk/api/messages/channels/"
URL_MSG = "https://supertiger.tk/api/messages/"
URL_STA = "https://supertiger.tk/api/settings/status"







class Channel(object):
    def __init__(self, channel):
        self._channel = channel
        with open('nertivia/constants.txt') as json_file:
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
        r = requests.get(url=str(URL_MSG + str(messageID) + '/channels/' + str(self._channel)), headers=headers1)
        message = Message(r.json())
        return message
      