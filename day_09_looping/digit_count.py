"""

write a program to display number of digits in a number

sample input:123
sample out:3

sample input:1234
sample out:4


read number

set digit_count as 0

repeat while number!=0:
    last_digit = number % 10
    update digit_count as digit_count+1
    update number as number // 10

display digit_count


"""

