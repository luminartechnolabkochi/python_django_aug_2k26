"""
1   E   1   E   1   E 
2   E   2   E   2   E
3   E   3   E   3   E

"""



for row in range(1,4):

    for col in range(1,7):

        if col%2==0:print("E",end="\t")
        else:print(row,end="\t")

    print()
