

arr = [1,3,2,5,4,7]
#      0 1 2 3 4 5
#               l r

arr.sort()

l = 0

while(l<len(arr)-1):

    r = l+1

    difference = arr[r] - arr[l]

    if difference!=1:

        print(arr[l]+1,"is missing")
        
        break
    l=l+1

