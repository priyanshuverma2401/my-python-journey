#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:      break and continue
#
# Author:      priyanshu verma
#
# Created:     15/11/2023
# Copyright:   (c) priyanshu verma 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

students = ["ram","shyam","kishan","radha","radhika"]

for student in students:
    if student == "radha":
        break;
    print(student)

for student in students:
    if student == "radha":
        continue;
    print(student)