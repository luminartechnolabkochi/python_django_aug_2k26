

nums = [3,4,5,8,1,7,6,1,2]
#       0 1 2 3 4 5 6 7 8
#         @ @ @

k = 3

max_sum = sum(nums[:k])

for window in range(1,len(nums)):

    cur_window_sum= sum(nums[window:window+k])

    print(cur_window_sum)

    if cur_window_sum > max_sum:

        max_sum=cur_window_sum

print(cur_window_sum)


