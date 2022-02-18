Code:

for row in range(7):
    for col in range(5):
        if (col == 0 and row != 0) or ((row == 0 or row == 3) and (col > 0 and col < 4)) or (col == 4 and (row == 1 or row == 2)) or ((row == col + 2) and (row > 3 and col > 0)):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

Output:

  * * *   
*       * 
*       *
* * * *
*   *
*     *
*       *
