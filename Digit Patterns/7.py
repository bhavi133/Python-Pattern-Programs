Code:

i = 1
j = 4
for row in range(7):
    for col in range(6):
        if (row == 0):
            print("*",end=" ")
        elif (row == i and col == j):
            print("*",end=" ")
            i +=1
            j -=1
        else:
            print(" ", end=" ")
    print()

Output:

* * * * * *
        *
      *     
    *
  *
*
