from nertivia.message import *
from nertivia.client import *
from nertivia.channel import *
from nertivia.user import *
import asyncio
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NTk0NDA0NjU3NjA1MzgyMTQ0IiwiaWF0IjoxNTcyMjI4NjkxMTAwfQ.P2Xzo-TssHRXRIF1_6ElfzupkKf103HndnKPXRHgojI" #YOUR TOKEN GOES HERE

client = Nertivia.client() #creates the client


@client.event #THIS EVENT IS REQUIRED you must have it or the bot will not work. This is hopefully temporary just while I find a better way to do this
def connect():
    client.emit('authentication', { 'token': token })
    print("I'm connected")

@client.event
def receiveMessage(message):
    c = Channel(6594395172002336768) #gets channel by ID
    m = Message(message) #gets the message info
    if str(m.authorID) != str(6594404657605382144): #checking if user is the bot
        if str(m.content) == '!testcommand': #simple on message commands until I make @client.command()
            c.send('Command test')
        else:
            c.send(f'{m.content} - {m.author}')
    else:
        return



Nertivia.login(client, token) #logs the bot in using the client and token
