Code:

for row in range(7):
    for col in range(5):
        if (col == 2) or (row == 6) or (row == 1 and col == 1) or (row == 2 and col == 0):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    
Output:

    *
  * *
*   *
    *
    *
    *
* * * * *
