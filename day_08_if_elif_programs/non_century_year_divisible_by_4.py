

"""
write a program to chk year is not ending with two 0's and divisible by 4


read year
chk year%100!=0 and year %4==0 then display year is leap year
"""

year = int(input("enter year"))

if year%100!=0 and year%4==0:

    print("leap year...")

else:

    print("not a leap year")