import discord

import responses
import datetime


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        if is_private:
            await message.author.reply(response) 
        else:
            if message.channel.send(response) != 'I didn\'t understand what you wrote. Try typing "!help".':
                await message.reply(response)
    except Exception as e:
        print(e)
async def channel_send(message, user_message, channel_id):
        await embed(user_message, channel_id, 0x00ff00)
async def embed(user_message, channel_id, color):
    embedVar = discord.Embed(title=user_message, color=color)
    await channel_id.send(embed=embedVar)
    




def run_discord_bot():
    TOKEN = ""
    with open("api.key", "r") as f:
        TOKEN = f.read()
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        user_id = str(message.author.id)
        channel_id = client.get_channel(1072313084267462746)
        timestamp = datetime.datetime.now().strftime("%I:%M:%S %p, on %B %d")
        await channel_send(message, (f'{username} ({user_id}) said: "{user_message}" in #{channel} at {timestamp})'), channel_id)
        
        
        
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
    @client.event
    async def on_member_join(member):
        send_message('filler', 'Hello, welcome to the server!', is_private=True)
    client.run(TOKEN)

run_discord_bot()