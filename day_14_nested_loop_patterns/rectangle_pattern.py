"""
#   #   # => row1 col3
#   #   # => row2 col3
#   #   # => row3 col3




*                   => row1 col1
*   *               => row2 col2
*   *   *           => row3 col3
*   *   *   *       => row4 col4
*   *   *   *   *   => row5 col5

repeat for row from 1 to 5:
    repeat for col from 1 to row:

        display *


"""


for row in range(1,6):

    for col in range(1,row+1):

        print("*",end=" ")

    print()
