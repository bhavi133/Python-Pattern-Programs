Code:

num = int(input("Input a number : "))

for row in range(num):
    for col in range(num):
        if (row == 0 or row == (num-1)) or (col == 0 or col == (num-1)):
            print("*", end="")
        else:
            print(" ", end="")
    print()

Output:

****
*  *
*  *
****
