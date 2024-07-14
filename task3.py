# Random password generater
import random
import string

def generate_password(length):
    # Define characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate random password using random.choices() method
    password = ''.join(random.choices(characters, k=length))

    return password

# Example usage
if __name__ == "__main__":
    print("Random Password Generator")
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Length must be a positive integer.")
            else:
                password = generate_password(length)
                print("Generated Password:", password)
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer for length.")
