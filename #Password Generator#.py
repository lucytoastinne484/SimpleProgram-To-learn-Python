#Password Generator#

import random

print("""""PASSWORD GENERATOR FOR PYTHON 
================================================""""")

chars = 'AaBcCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789!@#*_-+=#&¨`.<>:;)'



number= int(input('Put a number of passwords you wanna generate:         '))



password_lenght = int(input('Tell me what is the passwords\'s lenght:    '))




print('\n Here your passwords')


for pwd in range(number):
    passwords = ''
    for c in range(password_lenght):
        passwords += random.choice(chars)
        print(passwords)


