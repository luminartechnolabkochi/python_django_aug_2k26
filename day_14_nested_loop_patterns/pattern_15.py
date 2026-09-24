"""
5   5   5   5   5  row => 5 , col=>5
4   4   4   4       row => 4 , col=>4
3   3   3 
2   2
1



repeat for row from 5 to 1

    repeat col from 1 to row
        display  row
"""


for row in range(5,0,-1):

    for col in range(1,row+1):

        print(row,end=" ")

    print()
