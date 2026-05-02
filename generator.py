import string
import random
import argparse

def generate_password(length, use_digits=True, use_special=True, use_upper=True):
    characters = string.ascii_letters
    if not use_upper:   characters = characters.lower()
    if use_digits:  characters += string.digits
    if use_special: characters += string.punctuation
    
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

def main():
    print("--- PASSWORD GENERATOR ---")

    parser = argparse.ArgumentParser()
    parser.add_argument("--length", type=int, default=None)
    parser.add_argument("--no_digits", action="store_false", dest="use_digits")
    parser.add_argument("--no_special", action="store_false", dest="use_special")
    parser.add_argument("--no_upper", action="store_false", dest="use_upper")
    args = parser.parse_args()

    if args.length is None:
        length = int(input("Password length: "))
        digits = input("Contains digits (Y/N - default Y): ").strip().upper()
        use_digits = digits != "N"
        special = input("Contains special characters (Y/N - default Y): ").strip().upper()
        use_special = special != "N"
        upper = input("Contains upper cases (Y/N - default Y): ").strip().upper()
        use_upper = upper != "N"
    
        password_to_save = generate_password(length=length, use_digits=use_digits, use_special=use_special, use_upper=use_upper)
    else:
        password_to_save = generate_password(args.length, use_digits=args.use_digits, use_special=args.use_special, use_upper=args.use_upper)
        print(f"Generated password: {password_to_save}\n Saving to file...")

    with open("password.txt", "w") as f:
        f.write(password_to_save)

if __name__ == "__main__":
    main()