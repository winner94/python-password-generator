import string
import random

#print(string.ascii_letters)
#print(string.digits)
#print(string.punctuation)
#print(random.choice("abcdef"))
#

def generatore_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

print(generatore_password(8))