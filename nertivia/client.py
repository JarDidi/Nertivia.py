import requests 
import json
import asyncio
import abc
import logging
import socketio
import json


URL = "https://supertiger.tk/api/messages/channels/6594395172002336768"
URL_MSG = "https://supertiger.tk/api/messages/"

SOCKET_IP = "https://nertivia.supertiger.tk"






class Nertivia(object):
    def __init__(self, client):
        self.client = client
        with open('nertivia/constants.txt') as json_file:
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
        with open('nertivia/constants.txt', 'w') as outfile:
            json.dump(data, outfile)

        return client