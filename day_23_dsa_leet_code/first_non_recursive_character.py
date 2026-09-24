"""
Given a string s, 
find the first non-repeating character in it and return its index. If it does not exist, return -1

input:s="hello"


set s as hello

repeat for each char from s

    chk count of char in s ==1 then
        display index of char then exit
"""

s="loveleetcode"


for ch in s:

    if s.count(ch)==1:

        print(s.find(ch))

        break
else:

    print("-1")
