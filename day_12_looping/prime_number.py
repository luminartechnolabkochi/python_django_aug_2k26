"""
read number

set is_prime as True

repeat for i from 2 to number-1 

    chk if number%i==0 then
        update is_prime as False
        exit

display is_prime

"""

number = int(input("enter number   : "))

is_prime = True

for i in range(2,number):

    if number%i==0:

        is_prime=False

        break
print(is_prime)