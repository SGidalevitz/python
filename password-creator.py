import random

def def_constants():
    global characters
    global numbers
    global specialcharacters
    global possiblecharacters
    global original_file
    
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    specialcharacters = '!@#$%^&*()-=_+;<>,./?[]{}\|'
    possiblecharacters = characters * 2 #heavier bias towards characters
    
    with open('/Users/simon/Python stuff/projects/passmanager/passwords.txt', 'r') as passwords:
        original_file = passwords.read()  

def_constants()

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
def create_password_process():
    global possiblecharacters
    password = '' 
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
    return(scramble(password))
def add_password():
    password = create_password_process()
    
    with open('/Users/simon/Python stuff/projects/passmanager/passwords.txt', 'w') as passwords:
        password_purpose = input('What is this password for?')
        passwords.write(original_file)
        passwords.write(f'{password_purpose}: {password} \n')
    print('Added')

def remove_last_password(index):
    file_lines = original_file.split('\n')
    modified_file_list = [file_lines[i] for i in range(len(file_lines) - 1)]
    modified_file_list.pop(index)
    modified_file = ''
    for i in modified_file_list:
        modified_file += i
        modified_file += '\n'
    with open('/Users/simon/Python stuff/projects/passmanager/passwords.txt', 'w') as passwords:
        passwords.write(modified_file)
    print('Last Password Removed')

action = input('action?')
if action == '1':
    add_password()
if action == '2':
    while True:
        try:
            passindex = int(input('which password?')) - 1
            
        except:
            print('invalid index')
        
        file_lines = original_file.split('\n')
        modified_file_list = [file_lines[i] for i in range(len(file_lines) - 1)]
        if passindex <= len(modified_file_list) - 1:
            break
    remove_last_password(passindex)
            