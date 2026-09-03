"""
read num1,num2

set min_num as min(num1,num2)

repeat for i from 1 to min_num

    chk if num1%i==0 and num2%i==0 then
        display i

"""

num1 = int(input("enter number1 "))

num2 = int(input("enter number2 "))

min_num = min(num1,num2)

for i in range(1,min_num+1):

    if num1%i==0 and num2%i==0:

        print(i)



