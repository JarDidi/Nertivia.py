import nertivia
import asyncio
token = "TOKEN" #YOUR TOKEN GOES HERE

client = nertivia.Nertivia.client() #creates the client


@client.event #THIS EVENT IS REQUIRED you must have it or the bot will not work. This is hopefully temporary just while I find a better way to do this
def connect():
    client.emit('authentication', { 'token': token })
    print("I'm connected")

@client.event
def receiveMessage(message):
    c = nertivia.Channel(6594395172002336768) #gets channel by ID
    m = nertivia.Message(message) #gets the message info
    if str(m.authorID) != str(6594404657605382144): #checking if user is the bot
        if str(m.content) == '!testcommand': #simple on message commands until I make @client.command()
            c.send('Command test')
        elif '!user ' in str(m.content):
            userID = str(m.content).replace('!user ', '')
            user = nertivia.Nertivia.get_user(userID)
            c.send(f'{user.avatar_url} - {user.user}')
        else:
            c.send(f'{m.content} - {m.author}')
    else:
        return



nertivia.Nertivia.login(client, token) #logs the bot in using the client and token
