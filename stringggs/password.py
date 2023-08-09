# Prompt the user to input a password
password = input("Enter a password: ")

# Flag variables to track each condition
length_check = len(password) >= 8
space_check = False
uppercase_check = False
lowercase_check = False
special_check = False

# Check for spaces
for char in password:
    if char.isspace():
        space_check = True
        break

# Check for uppercase letters
for char in password:
    if char.isupper():
        uppercase_check = True
        break

# Check for lowercase letters
for char in password:
    if char.islower():
        lowercase_check = True
        break

# Check for special characters
special_characters = ['-', '@', '#', '$', '%', '^', '&', '*', '!', '?']
for char in password:
    if char in special_characters:
        special_check = True
        break

# Check each condition and provide appropriate feedback
if not length_check:
    print("Password must be at least 8 characters long.")
elif space_check:
    print("Password cannot contain spaces.")
elif not uppercase_check:
    print("Password must contain at least 1 uppercase letter.")
elif not lowercase_check:
    print("Password must contain at least 1 lowercase letter.")
elif not special_check:
    print("Password must contain at least 1 special character (i.e. - @ # $ % ^ & * ! ?).")
else:
    print("Password is valid.")
