#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:      list
#
# Author:      priyanshu verma
#
# Created:     15/11/2023
# Copyright:   (c) priyanshu verma 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

marks = [95,98,97]

print(marks[-2])
print(marks[2])

print(marks[0:2])

for score in marks :
    print(score)

marks.append(99)

for score in marks:
    print(score)

marks.insert(0,90)

print(90 in marks)
for score in marks:
    print(score)

print(len(marks))

i=0
while i<len(marks):
    print(marks[i])
    i=i+1
marks.clear();

for score in marks:
    print(score)

print(marks[2]) #index out of range error


