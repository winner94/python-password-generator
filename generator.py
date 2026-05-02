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
    password_dict = dict()
    print("--- PASSWORD GENERATOR ---")
    suggestion_count = int(input("How many password suggestions you want? "))
    
    for i in range(1, suggestion_count+1):
        length = random.randint(8, 20)
        password_dict[i] = generate_password(length)

    for k, v in password_dict.items():
        print(f"{k}: {v}") 

    password_to_save = int(input(f"Which one to save 1-{suggestion_count}: "))
    
    with open("password.txt", "w") as f:
        f.write(password_dict[password_to_save])

if __name__ == "__main__":
    main()

# print(generatore_password(8))
# print(generatore_password(12, use_digits=False))
# print(generatore_password(8, use_special=False))
# print(generatore_password(8, use_upper=False))