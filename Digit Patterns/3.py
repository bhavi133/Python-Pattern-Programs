Code:

for row in range(7):
    for col in range(6):
        if ((row == 0 or row == 3 or row == 6) and (col > 0 and col < 5)) or (col == 5 and (row != 0 and row != 3 and row != 6)) or (col == 0 and (row == 1 or row == 5)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

Output:

  * * * *
*         *
          *
  * * * *
          *
*         *
  * * * *
