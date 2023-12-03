#Welcome to my Password Generator
#This program is capable of generating strong passwords of any desired length

#import random for access to random.choice
import random
#Greeting
print("Hello I am Your personal Password Generator!")

#Establish usable characters
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789"

#prompts the user to input amount of passwords needed
#converts input for number into integer
number = input("Enter amount of passwords to generate: ")
number = int(number)

#prompts user for desired password length
#converts input for length into integer
length = input("Enter length of Password: ")
length =int(length)

#/n to add a new line before displaying passwords
print("\nHere are your passwords:")

#for loop used to generate password
for pswd in range(number):
    passwords = ""
    for char in range(length):
        passwords += random.choice(chars)
    print(passwords)