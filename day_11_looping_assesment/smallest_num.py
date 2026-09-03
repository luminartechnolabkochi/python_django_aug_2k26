"""
smallest number amoung 5

set small_num as None

repeat for i from 1 to 5

    read number

    chk if number < small_num or small_num == None then
        update small_numner as number

"""

small_num = None

for i in range(1,6):

    number = int(input("enter number"))

    if small_num == None or number < small_num:

        small_num = number

print(small_num)



"""
sum of n numbers

sum of n odd_numbers

sum of even_numbers

leap year from 1800 to 2026

common divisors of a number 8 => 1,2,4,8| 6 => 1,2,3,6

common divisors of two number => 8,24 [1,2,4,8]

gcd of two number => 8,24 [8]

prime number  => 8 ❌  , 19 =>[1,19]✅ , 9 [1,3,9] ❌, 13 [1,13] ✅

fibonacci series => 0 1 1 2 3 5 8 13 21 34.....

armstrong number: 
                153 [1^3 + 5^3 + 3^3] = 153 , 370 [3^3 + 7^3 + 0^3] 27+343+0

                1634 [1^4 + 6^4 + 3^4 + 4^4]= 1634
Factorial : 

phase1 exam will be on saturday offline mode : futuremug 

python interpreter

variables and data types
operators (A.O,R.O,L.O,M.O,I.O)
decision making (if, if..else,if..elif..else,match..case)
looping (while,for)

"""