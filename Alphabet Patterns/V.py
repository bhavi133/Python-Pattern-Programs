Code:

i = 0
j = 6
for row in range(4):
    for col in range(7):
        if (col == row):
            print("*", end=" ")
        elif (row == i and col == j):
            i += 1
            j -= 1
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

Output:

*           * 
  *       *   
    *   *
      *
