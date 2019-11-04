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

        with open('nertivia/constants.txt') as json_file:
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

    def testRequest(self, channel):
        r = requests.get(url=str(URL + str(channel)), headers=self.headers)
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
        r = requests.patch(url=str(URL_MSG + str(self.id) + '/channels/' + str(channel)), headers=headers1, data=json.dumps(data))

    def changeStatus(token, status):
        data = {'status': status,
                'tempID': 0}  
        r = requests.post(url=URL_STA, headers=self.headers, data=json.dumps(data))      
