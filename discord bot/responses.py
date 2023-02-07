import random
import openai
from googletrans import Translator
import discord
openai.api_key = ""
with open("openaiapi.key", "r") as f:
    openai.api_key = f.read()


def translate(dest_language, text):
    translator = Translator(service_urls=['translate.google.com'])
    result = translator.translate(text, dest=dest_language)
    return result


# privet russian
def get_response(message: str) -> str:
    p_message = message.lower()
    if p_message.startswith('!'):
        if p_message == '!hello':
            return 'Hey it works!'
        if p_message == '!flip':
            return "heads" if random.randint(1,2) == 1 else "tails"
        if p_message == '!roll':
            return str(random.randint(1, 6))
        if p_message.startswith('!translate'):
            language = message.split(' ')[1]
            return translate(language, message[len("!translate") + len(language):])
        if p_message == '!help':
            return ""
        if p_message.startswith('!math'):
            return int(p_message[5:])
        if p_message == '!restart':
            import bot
            exit()
        if p_message == '!kill':
            exit()
        if p_message.startswith("!cgpt"):
            completion = openai.Completion.create(engine="text-davinci-003", prompt=p_message[5:], temperature = 0)
            return completion.choices[0].text
        if p_message == '!guild':
            return 'hello'
            #discord.get_guild()
        return 'I didn\'t understand what you wrote. Try typing "!help".'
    