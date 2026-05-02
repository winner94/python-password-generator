import string
import random

#print(string.ascii_letters)
#print(string.digits)
#print(string.punctuation)
#print(random.choice("abcdef"))
#

def generatore_password(length, use_digits=True, use_special=True, use_upper=True):
    #characters = string.ascii_letters + string.digits + string.punctuation
    characters = string.ascii_letters
    if use_upper:   characters = characters.lower()
    if use_digits:  characters += string.digits
    if use_special: characters += string.punctuation
    
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

print(generatore_password(8))
print(generatore_password(12, use_digits=False))
print(generatore_password(8, use_special=False))
print(generatore_password(8, use_upper=False))