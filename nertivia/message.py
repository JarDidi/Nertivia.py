import requests 
import json
import asyncio
import abc

URL = "https://supertiger.tk/api/messages/channels/"
URL_MSG = "https://supertiger.tk/api/messages/"
URL_STA = "https://supertiger.tk/api/settings/status"






class Message():

    def __init__(self, message):
        self.id = message['message']['messageID']
        self.content = message['message']['message']
        self.authorName = message['message']['creator']['username']
        self.author = message['message']['creator']['username'] + '@' + message['message']['creator']['tag']
        self.authorID = message['message']['creator']['uniqueID']

        with open('constants.txt') as json_file:
            data = json.load(json_file)
            for p in data['constants']:
                self.token = p['token']

        self.headers = {'Accept': 'text/plain',
                'authorization': self.token,
                'Content-Type': 'application/json;charset=utf-8'}

    @property
    def _id(self):
        return self.id
    
    @property
    def _content(self):
        return self.content

    @property
    def _author(self):
        return self.author

    @property
    def _author_name(self):
        return self.authorName
    
    @property
    def _author_id(self):
        return self.authorID

    @staticmethod
    def testRequest(channel):
        with open('constants.txt') as json_file:
            data = json.load(json_file)
            for p in data['constants']:
                token = p['token']

        headers = {'Accept': 'text/plain',
                'authorization': token,
                'Content-Type': 'application/json;charset=utf-8'}
        r = requests.get(url=str(URL + str(channel)), headers=headers)
        return r.headers.get('set-cookie')

    def edit(self,channel, content):
        sid = Message.testRequest(channel=channel)
        sid = sid.split('connect.sid=', 1)[1].strip('; Path=/; HttpOnly')
        data = {'message': content,
                'tempID': 0}
                
        headers1 = {'Accept': 'text/plain',
                    'authorization': self.token,
                    'Content-Type': 'application/json;charset=utf-8',
                    'Cookie': f'connect.sid={sid}' } 
        requests.patch(url=str(URL_MSG + str(self.id) + '/channels/' + str(channel)), headers=headers1, data=json.dumps(data))

    def delete(self, channel):
        sid = Message(self).testRequest(channel=channel)
        sid = sid.split('connect.sid=', 1)[1].strip('; Path=/; HttpOnly')
                
        headers1 = {'Accept': 'text/plain',
                    'authorization': self.token,
                    'Content-Type': 'application/json;charset=utf-8',
                    'Cookie': f'connect.sid={sid}' } 
        requests.delete(url=str(URL_MSG + str(self.id) + '/channels/' + str(channel)), headers=headers1)

    def changeStatus(self, token, status):
        data = {'status': status,
                'tempID': 0}  
        r = requests.post(url=URL_STA, headers=self.headers, data=json.dumps(data))      
