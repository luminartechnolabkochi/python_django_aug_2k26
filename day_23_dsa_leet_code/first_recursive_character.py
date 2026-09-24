"""
first repeating character in a string

input: s="leetcode"

output:a


step1: set s as leetcode 
step2: create an empty list as lst
step3:repeat for each char in s
    step4:chk if char not in lst then
            step5: add char to lst
            else display char then exit

"""


s ="helloworld"

lst =[]
for char in s:

    if char not in lst:

        lst.append(char)
    else:

        print("first recursive character is ",char)

        break