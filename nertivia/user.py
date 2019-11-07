import asyncio
import requests
import json



class User(object):
    def __init__(self, user):
        self.id = user['user']['uniqueID']
        self.username = user['user']['username']
        self.avatar_url = "https://supertiger.tk/api/avatars/{}".format(user['user']['avatar'])
        self.user = "{}@{}".format(user['user']['username'], user['user']['tag'])
    
    @property
    def _id(self):
        return self.id

    @property
    def _name(self):
        return self.username

    @property
    def _avatar_url(self):
        return self.avatar_url
    
    @property
    def _user(self):
        return self.user