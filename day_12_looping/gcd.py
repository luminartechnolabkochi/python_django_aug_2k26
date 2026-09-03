

"""
gcd of two number => 8,24 [8]

read num1,num2

set gcd as 1    

set small_num as minimum of num1 and num2

repeat for i from 2 to small_num 
    chk if num1 % i == 0 and num2 % i == 0 then
        update gcd as i
display gcd

"""

num1 = int(input("enter num1"))

num2 = int(input("enter num2"))

small_num = min(num1,num2)

gcd = 1

for i in range(2,small_num+1):

    if num1%i==0 and num2%i==0:

        gcd = i

print(gcd)


