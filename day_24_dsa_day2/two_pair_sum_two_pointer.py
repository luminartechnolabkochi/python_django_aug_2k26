

"""
arr =[1,4,2,3,7,6]

target=9

set left as 0

set right as len(arr)-1

repeat while left < right:
    calculate cur_sum as arr[left] + arr[right]
    case1: chk target == cur_sum then display arr[left] and arr[right] exit
    case2:chk cur_sum > target then update right as right -1
    case3:chk cur_sum < target then update left as left + 1


"""

arr=[1,3,2,5,4,7,6]

arr.sort()

target = 11

left = 0

right = len(arr)-1

while(left<right):

    cur_sum = arr[left] + arr[right]

    if cur_sum == target:

        print(arr[left],arr[right],"pair")

        break

    elif cur_sum > target:

        right = right -1

    elif cur_sum < target:

        left = left+1

