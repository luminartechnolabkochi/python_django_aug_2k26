"""
write a program to chk year is / by 100 and year / by 400 then display
century leap year

"""


year = int(input("enter year"))

if year%100==0 and year%400==0:

    print("century leap year")

else:

    print("not a century leap year")