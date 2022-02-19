Code:

i = 1
j = 3
for row in range(7):
    for col in range(7):
        if col == 4 or row == 4 :
            print("*", end=" ")
        elif row == i and col == j:
            print("*",end=" ")
            i += 1
            j -= 1
        else:
            print(" ", end=" ")
    print()

Output:

        *
      * *
    *   *
  *     *
* * * * * * *
        *
        *
