import random
import openai

openai.api_key = "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"



def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey it works!'
    
    if message == 'roll':
        return str(random.randint(1, 6))
    
    if p_message == '!help':
        return "`This is a help message that you can modify.`"
    if p_message.startswith("cgpt"):
        completion = openai.Completion.create(engine="davinci", prompt=p_message[5:])
        return completion.choices[0].text
    
    
    return 'I didn\'t understand what you wrote. Try typing "!help".'
    