import string
import random

#print(string.ascii_letters)
#print(string.digits)
#print(string.punctuation)
#print(random.choice("abcdef"))
#

def generate_password(length, use_digits=True, use_special=True, use_upper=True):
    #characters = string.ascii_letters + string.digits + string.punctuation
    characters = string.ascii_letters
    if use_upper:   characters = characters.lower()
    if use_digits:  characters += string.digits
    if use_special: characters += string.punctuation
    
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

def main():
    length = int(input("Password length: "))
    digits = input("Contains digits (Y/N - default Y): ").strip().upper()
    use_digits = digits != "N"
    special = input("Contains special characters (Y/N - default Y): ").strip().upper()
    use_special = special != "N"
    upper = input("Contains upper cases (Y/N - default Y): ").strip().upper()
    use_upper = upper != "N"
    
    generated_password = generate_password(length, use_digits, use_special, use_upper)
    with open("password.txt", "wt") as f:
        f.write(generated_password)

if __name__ == "__main__":
    main()

# print(generatore_password(8))
# print(generatore_password(12, use_digits=False))
# print(generatore_password(8, use_special=False))
# print(generatore_password(8, use_upper=False))