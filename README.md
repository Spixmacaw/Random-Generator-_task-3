<h1># Random-Generator-_task-3</h1>

Random Password Generator

    A simple Python script to generate random passwords of specified lengths. This tool helps you create secure passwords for your accounts.

## Features

    - Generates random passwords using uppercase and lowercase letters, digits, and punctuation.
    - User-friendly interface that prompts for the desired password length.
    - Validates input to ensure the length is a positive integer.

## Requirements

    - Python 3.x

## Usage

    1. Clone the repository:
       ```bash
          git clone https://github.com/yourusername/random-password-generator.git
          
      cd random-password-generator
      
Run the script:

  1. bash

         python password_generator.py
      
  2.Enter the desired length of the password when prompted.

Example Output : 

     Random Password Generator
     Enter the length of the password: 12
     Generated Password: b#A5^dF!2&gH

     
Source Code snipet : 

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

![Spixmacaw's Stats](https://github-readme-stats.vercel.app/api?username=Spixmacaw&theme=tokyonight&show_icons=true&hide_border=true&count_private=true)

<p><img align="center" width="470" height="" src="https://github-readme-streak-stats.herokuapp.com/?user=Spixmacaw&theme=tokyonight&hide_border=true" alt="Spixmacaw" /></p>

![Spixmacaw's Stats](https://github-readme-stats.vercel.app/api/top-langs/?username=Spixmacaw&theme=tokyonight&show_icons=true&hide_border=true&layout=compact)

<hr>

![Alt](https://repobeats.axiom.co/api/embed/76e6ef55d852b53769aeeb80da65d582e1067fa0.svg "Repobeats analytics image")
