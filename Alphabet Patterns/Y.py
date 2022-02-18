Code:

for row in range(5):
    for col in range(5):
        if ((row == col) and (row < 2)) or ((col == 2) and (row > 1)) or ((row == 0 and col == 4) or (row == 1 and col == 3)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

Output:

*       * 
  *   *   
    *
    *
    *
