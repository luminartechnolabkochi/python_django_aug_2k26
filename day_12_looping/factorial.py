

"""
read number

set factorial as 1

repeat for i from 1 to number

    update factorial as factorial * i

display factorial

"""

number = int(input("enter number..... "))

factorial = 1

for i in range(1,number+1):

    factorial = factorial*i

print(factorial)