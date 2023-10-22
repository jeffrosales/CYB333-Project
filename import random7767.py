import random
import string
import getpass  # For secure password input
import re  # Regular expressions for pattern matching
import hashlib  # For hashing the master password
import os  # For checking if a file exists

MASTER_PASSWORD_FILE = "master_password.txt"

def set_master_password():
    master_password = getpass.getpass("Set your master password: ")
    hashed_password = hashlib.sha256(master_password.encode()).hexdigest()
    with open(MASTER_PASSWORD_FILE, 'w') as file:
        file.write(hashed_password)

def check_master_password():
    if not os.path.exists(MASTER_PASSWORD_FILE):
        set_master_password()
    hashed_password = ""
    with open(MASTER_PASSWORD_FILE, 'r') as file:
        hashed_password = file.read().strip()
    entered_password = getpass.getpass("Enter your master password: ")
    if hashlib.sha256(entered_password.encode()).hexdigest() == hashed_password:
        return True
    return False

def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(site, username, password):
    with open('passwords.txt', 'a') as file:
        file.write(f"Site: {site}\nUsername: {username}\nPassword: {password}\n\n")

def retrieve_passwords():
    try:
        with open('passwords.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "No passwords saved yet."

def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    elif (re.search('[a-z]', password) and
          re.search('[A-Z]', password) and
          re.search('[0-9]', password) and
          re.search('[^a-zA-Z0-9]', password)):
        return "Strong"
    else:
        return "Moderate"

def estimate_break_time(password):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    total_combinations = len(characters) ** len(password)
    guesses_per_second = 10**10  # 10 billion guesses
    total_seconds = total_combinations / guesses_per_second
    years = total_seconds / (60 * 60 * 24 * 365.25)  # Convert seconds to years
    return years

if __name__ == "__main__":
    if not check_master_password():
        print("Incorrect master password. Access denied.")
        exit()

    while True:
        print("Password Manager Menu:")
        print("1. Generate a new password")
        print("2. Save a password")
        print("3. Retrieve saved passwords")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            length = int(input("Enter the desired password length: "))
            use_upper = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
            use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
            use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
            password = generate_password(length, use_upper, use_digits, use_special)
            strength = check_password_strength(password)
            break_time = estimate_break_time(password)
            print(f"Generated Password: {password}")
            print(f"Password Strength: {strength}")
            print(f"Estimated time to break (using brute force): {break_time:.2f} years\n")

        elif choice == '2':
            site = input("Enter the site or service name: ")
            username = input("Enter the username: ")
            password = getpass.getpass("Enter the password: ")  # Secure password input
            save_password(site, username, password)
            print("Password saved successfully.\n")

        elif choice == '3':
            passwords = retrieve_passwords()
            print("Saved Passwords:\n")
            print(passwords)

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please select a valid option.\n")
