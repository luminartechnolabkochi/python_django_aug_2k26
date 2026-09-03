"""
read number

set digit_count as len(str(number))

set result as 0

repeat while number !=0

    set digit as number % 10

    set exponent  as digit ** digit_count

    update result as result + exponent

    update number as number // 10

display result

"""

number = int(input("enter number . "))

digit_count = len(str(number))

result = 0

while(number!=0):

    digit = number % 10

    exponent = digit ** digit_count

    result = result + exponent

    number = number // 10

print(result)