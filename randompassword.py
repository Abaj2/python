import string
import random

def password_generator(length):
    characters = string.ascii_letters + string.punctuation + string.digits
    password = ''.join(random.choice(characters) for i in range (length))
    return password

while True:
    try:
        length =int(input("Enter the length of the password: "))
        break
    except ValueError:
        length = (input('Enter an integer value: '))


password = password_generator(length)
print('Your password is:', password)



