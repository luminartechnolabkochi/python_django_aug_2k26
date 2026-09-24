
"""

*   2   *   4
*   2   *   4
*   2   *   4
*   2   *   4

"""

for row in range(1,5):

    for col in range(1,5):

        if col%2!=0:print("*",end="\t")
        else:print(col,end="\t")

    print()

