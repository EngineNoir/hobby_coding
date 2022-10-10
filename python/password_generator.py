import random

def password_of_length():
    # ord('!') = 33 and ord('/') = 47
    # ord('0') = 48 and ord('9') = 57 --> 3
    # ord(':') = 58 and ord('`') = 96
    # ord('A') = 65 and ord('Z') = 90 --> 1
    # ord('[') = 91 and ord('`') = 96
    # ord('a') = 97 and ord('z') = 122 --> 2
    # ord('{') = 123 and ord('~') = 126

    n = int(input('What is the length of the password: '))
    x = input('Include numbers (Y/N)? ')
    y = input('Include symbols (Y/N)? ')

    range_choices = [1]
    i = 0
    password = ''

    if x == 'Y':
        range_choices.append(2)
    if y == 'Y':
        range_choices.append(3)

    while i < n:

        range_choice = random.choice(range_choices)

        if range_choice == 1:
            password += str(chr(random.choice([random.randint(65, 90), random.randint(97, 122)])))
        elif range_choice == 2:
            password += str(chr(random.randint(48, 57)))
        elif range_choice == 3:
            password += str(chr(random.choice([random.randint(33, 47), random.randint(58, 126)])))

        i += 1

    print(password)
    print('\n')
    password_of_length()


password_of_length()
