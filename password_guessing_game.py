#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:      basic number guessing game
#
# Author:      priyanshu verma
#
# Created:     15/11/2023
# Copyright:   (c) priyanshu verma 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

def guess_number():
    secret_number = random.randint(1,100)
    print("welcome to the number guessing game! ")
    print("secrete number is in between 1 and 100\n")
    attempt =0

    while True:
        guess = int(input("enter your guess : "));
        attempt+=1

        if guess == secret_number:
            print("congratulations! you won")
        elif guess < secret_number :
            print(" low ! try again:\n")
        else:
            print("high ! try again\n")

guess_number()

