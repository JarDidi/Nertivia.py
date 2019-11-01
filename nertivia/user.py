import asyncio
import requests
import json

with open('nertivia/constants.txt') as json_file:
    data = json.load(json_file)
    for p in data['constants']:
        token = p['token']

class User(object):
    def __init__(self):
        headers = {'Accept': 'text/plain',
                    'authorization': token,
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
    
