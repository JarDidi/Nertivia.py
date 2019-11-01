import requests 
import json
import asyncio
import abc
import logging
import socketio
import json

with open('nertivia/constants.txt') as json_file:
    data = json.load(json_file)
    for p in data['constants']:
        token = p['token']

URL = "https://supertiger.tk/api/messages/channels/6594395172002336768"
URL_MSG = "https://supertiger.tk/api/messages/"

SOCKET_IP = "https://nertivia.supertiger.tk"

headers = {'Accept': 'text/plain',
           'authorization': token,
           'Content-Type': 'application/json;charset=utf-8'}




class Nertivia(object):
    def __init__(self, client):
        self.client = client

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