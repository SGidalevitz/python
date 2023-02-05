import discord

TOKEN = "MTA3MTIxMjI4MzczMDA3MTYwMg.GKj5NX.G7o6Mrxa6IrajC9wiNV7hwgYTuGSB7IzNsntI8"

intents = discord.Intents.default()
intents.guilds = True
intents.members = False
intents.presences = False
intents.messages = True



client = discord.Client(intents=intents)


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("{0.user} is online!".format(client))

@client.event
async def on_message(message):
    try:
        if message.content == "!hello":
            await message.channel.send("jusates")
    except Exception as e:
        print("An error occurred:", e)


client.run(TOKEN)
