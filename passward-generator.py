import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    character_pool = ''
    
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password (8-128): "))
            if 8 <= length <= 128:
                break
            else:
                print("Please enter a length between 8 and 128.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get user preferences for password complexity
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate the password
    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        print(f"\nGenerated Password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
