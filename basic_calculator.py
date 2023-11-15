#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:      basic calculator
#
# Author:      priyanshu verma
#
# Created:     15/11/2023
# Copyright:   (c) priyanshu verma 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

first = input("enter the first operand")
operator = input("enter operator: ")
second = input("enter second operand: ")

first=int(first)
second = int(second)

if operator == "+" :
    print(first + second)
elif operator == "-" :
    print(first - second)
elif operator=="*" :
    print(first * second)
elif operator == "/" :
    print(first / second)
else :
    print("invalid operator or operand")

