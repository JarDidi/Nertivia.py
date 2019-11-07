import requests 
import json
import asyncio
import socketio


URL = "https://supertiger.tk/api/messages/channels/6594395172002336768"
URL_MSG = "https://supertiger.tk/api/messages/"

SOCKET_IP = "https://nertivia.supertiger.tk"






class Nertivia(object):
    def __init__(self, client):
        self.client = client
        with open('constants.txt') as json_file:
            data = json.load(json_file)
            for p in data['constants']:
                self.token = p['token']

        self.headers = {'Accept': 'text/plain',
                'authorization': self.token,
                'Content-Type': 'application/json;charset=utf-8'}


    def client():
        return socketio.Client()
    
    @staticmethod
    def login(client, token):
        client.emit('authentication', { 'token': token })
        client.connect(SOCKET_IP)
        data = {}
        data['constants'] = []
        data['constants'].append(
            {'token': token}
        )
        with open('constants.txt', 'w') as outfile:
            json.dump(data, outfile)

        return client

    @staticmethod
    def get_user(userID):
        with open('constants.txt') as json_file:
            data = json.load(json_file)
            for p in data['constants']:
                token = p['token']

        headers = {'Accept': 'text/plain',
                'authorization': token,
                'Content-Type': 'application/json;charset=utf-8'}
        r1 = requests.get(url=f'https://supertiger.tk/api/user/{userID}', headers=headers)
        user = r1.json()
        return user