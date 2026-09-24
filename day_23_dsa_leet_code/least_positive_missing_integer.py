

"""
arr =[1,2,3,5]

"""
arr =[1,2,4]

min_num = min(arr)

max_num = max(arr)

total = 0

for n in range(min_num,max_num+1):

    total = total + n


arr_sum = sum(arr)

if total!=arr_sum:

    print(total - arr_sum,"missing")

else:

    print("no missing")



