
"""
write a program to display first common divisor of a number except 1 and same number

read number

repeat for i from 2 to number-1

    chk if number % i==0 then
        display number
        exit from loop

"""

number = int(input("enter number   ."))

for i in range(2,number):

    if number%i==0:

        print(i)

        break