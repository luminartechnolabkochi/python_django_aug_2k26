
"""
O   E   O   E   O
O   E   O   E   O
O   E   O   E   O
O   E   O   E   O

"""


for row in range(1,5):

    for col in range(1,6):

        if col%2!=0:print("O",end="\t")

        else:print("E",end="\t")

    print()
