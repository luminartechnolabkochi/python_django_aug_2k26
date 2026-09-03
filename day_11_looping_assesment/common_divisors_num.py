"""
common divisors of a number

read number

repeat for i from 1 to number
    chk if number % i ==0 then
        display i

"""



number = int(input("enter number...."))

for i in range(1,number+1):

    if number % i ==0:
        print(i)