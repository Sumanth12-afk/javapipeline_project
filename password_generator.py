import random
import string

def generate_password(length, include_lowercase, include_uppercase, include_digits, include_special):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    character_pool = ''
    if include_lowercase:
        character_pool += lowercase
    if include_uppercase:
        character_pool += uppercase
    if include_digits:
        character_pool += digits
    if include_special:
        character_pool += special

    if not character_pool:
        return "Error: No character sets selected."

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the desired length of the password: "))
        include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
        include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        include_special = input("Include special characters? (yes/no): ").lower() == 'yes'

        password = generate_password(length, include_lowercase, include_uppercase, include_digits, include_special)
        print("Generated Password: ", password)
    
    except ValueError:
        print("Invalid input! Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()

