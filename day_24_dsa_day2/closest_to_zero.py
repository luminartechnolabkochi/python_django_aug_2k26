


"""
Given an integer array nums of size n, return the number with the value closest to 0 in nums. 
If there are multiple answers, return the number with the largest value.

"""

nums = [-2,-3,2,3]

closest = nums[0]

for num in nums:

    if abs(num) < abs(closest):

        closest = num # -2

if closest < 0 and abs(closest) in nums:

    print(abs(closest))

else:

    print(closest)