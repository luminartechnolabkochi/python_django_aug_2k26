"""
set big_num as 0

repeat for i from 1 to 5:

    read number

    chk number> big_num then 
        update big_num as number
"""

big_number = 0

for i in range(1,6):

    number = int(input("enter number "))

    if number > big_number:

        big_number = number

print(big_number)