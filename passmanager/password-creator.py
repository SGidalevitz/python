import random
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
specialcharacters = '!@#$%^&*()-=_+;<>,./?[]{}\|'
#heavier bias towards characters1
possiblecharacters = characters + characters
password = ''

with open('/Users/simon/Python stuff/projects/Tic-tac-toe-fr.py', 'r') as passmanager:
    print(passmanager.read())

while True:
    try:
        number = int((input('Does the password require a number? (0: No, 1: Yes)')))
    except:
        print('number must be an integer')
        continue
    if number == 0 or number == 1:
        break
    print('Input must be 0 or 1')
while True:
    try:
        specialcharacter = int((input('Does the password require a special character? (0: No, 1: Yes)')))
    except:
        print('number must be an integer')
        continue
    if specialcharacter == 0 or specialcharacter == 1:
        break
    print('Input must be 0 or 1')
while True:
    try:
        minlength = int((input('What is the minimum length of this password? (Input an integer)')))
    except:
        print('number must be an integer')
        continue
    if minlength > 0:
        break
    print('Input must be greater than 0')

if number:
    possiblecharacters += numbers
    password += numbers[random.randrange(len(numbers) - 1)]
if specialcharacter:
    possiblecharacters += specialcharacters
    password += specialcharacters[random.randrange(len(specialcharacters) - 1)]

remaining_characters = minlength - (number + specialcharacter)

for i in range(int(1.5 * (remaining_characters))):
    password += possiblecharacters[random.randrange(len(possiblecharacters) - 1)]


def scramble(string):
    scramblecharacters = [i for i in string]
    scrambleoutput = ''
    while len(scramblecharacters) > 1:
        scramblenumber = random.randrange(len(scramblecharacters) - 1)
        scrambleletter = scramblecharacters[scramblenumber]
        scrambleoutput += scrambleletter
        scramblecharacters.pop(scramblenumber)
    scrambleoutput += scramblecharacters[0]

    return scrambleoutput

print(scramble(password))
        
