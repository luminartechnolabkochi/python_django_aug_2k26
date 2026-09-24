"""
reverse a given list without using reverse and slicing


arr =[1,10,2,200,3,300]

output:[300,3,200,2,10,1]
"""

arr =[1,10,2,200,3,300]

left = 0

right = len(arr)-1

while(left < right):

    (arr[left],arr[right]) = (arr[right],arr[left])

    left +=1

    right -=1

print(arr)


# reverse=[]

# for i in range(0,len(arr)):

#     popped_element = arr.pop()
#     reverse.append(popped_element)

# print(reverse)
