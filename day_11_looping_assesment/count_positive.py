"""
Count Positive Numbers


"""

p_count =0
for i in range(1,6):

    number = int(input("enter number"))

    if number > 0: 
        p_count = p_count+1

print(p_count)