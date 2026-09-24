
"""
two pair sum 

arr=[2,3,4,5,6]

target=9 

"""

arr=[2,3,4,5,6]

target = 9 

for num in arr:

    difference = target - num

    if difference in arr:

        print(num,difference)

        break


"""

two pointer algorithm

"""