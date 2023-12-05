import string
import random

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(number_of_passwords=5, length=12):
    passwords = [generate_password(length) for _ in range(number_of_passwords)]
    return passwords

def print_generated_passwords(passwords):
    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")

def main():
    print("Welcome to the Secure Password Generator!")

    # Get user input for password length
    while True:
        length = int(input("Enter the desired password length (at least 12 characters recommended): "))
        if length >= 12:
            break
        else:
            print("Password length should be 12 or greater. Please try again!!.")

    # Get user input for the number of passwords to generate
    number_of_passwords = int(input("Enter the number of passwords to generate: "))

    # Generate passwords
    passwords = generate_multiple_passwords(number_of_passwords, length)

    # Print the generated passwords
    print_generated_passwords(passwords)

if __name__ == "__main__":
    main()
