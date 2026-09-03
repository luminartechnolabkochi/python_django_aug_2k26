"""
extract digit in reverse order ie number = 125 o/p 5 2 1

read number

repeat while number!=0 

    last_digit = number % 10
    display last_digit
    update number as number // 10

"""


number = int(input("enter number.... "))

while number!=0:

    last_digit = number % 10

    print(last_digit)

    number = number // 10


"""
write a program to display number of digits in a number

sample input:123
sample out:3

sample input:1234
sample out:4
"""