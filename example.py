from nertivia.message import *
from nertivia.client import *
from nertivia.channel import *
from nertivia.user import *
import asyncio
token = "TOKEN"

client = Nertivia.client()


@client.event
def connect():
    client.emit('authentication', { 'token': token })
    print("I'm connected")

@client.event
def receiveMessage(message):
    c = Channel(6594395172002336768)
    m = Message(message)
    if str(m.authorID) != str(6594404657605382144):
        if str(m.content) == '!testcommand':
            c.send('Command test')
        elif str(m.content) == '!editMessage':
            mess = c.get_message(6595857507611054080)
            mess.edit(channel, 'Testing Edit')
        else:
            c.send(f'{m.content} - {m.author}')
    else:
        return



Nertivia.login(client, token)
