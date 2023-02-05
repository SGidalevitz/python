import openai
openai.api_key = "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"

list = []


# create a completion
for x in range(1):
    completion = openai.Completion.create(engine="ada", prompt="what is the square root of 16?")
    list.append(completion.choices[0].text)

for x in list:
    print(x)