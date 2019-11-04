import asyncio
import requests
import json



class User(object):
    def __init__(self):
        with open('constants.txt') as json_file:
            data = json.load(json_file)
            for p in data['constants']:
                self.token = p['token']

        self.headers = {'Accept': 'text/plain',
                'authorization': self.token,
                'Content-Type': 'application/json;charset=utf-8'}
        r1 = requests.get(url='https://supertiger.tk/api/user', headers=headers)
        dataa = r1.json()
        self.id = dataa['user']['uniqueID']
        self.username = dataa['user']['username']
    
    @property
    def _id(self):
        return self.id

    @property
    def _name(self):
        return self.username
    
