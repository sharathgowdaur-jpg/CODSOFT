import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.punctuation + string.digits
    password=""

    for i in range(length):
        password+=random.choice(characters)
    return password

print("===========Password Generator menu from codsoft==========")


try:
    length=int(input("enter the length of password you want to generate:"))

    if length<=8:
        print("The length should be greater than 8 or more!")

    else:
        password=generate_password(length)
        print(f"Your generated password is: {password}")

except ValueError:
    print("Invalid input! please enter a valid integer for password length!")
