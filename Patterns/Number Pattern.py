lst1 = []

def pattern():
    for i in range(len(name)):
        # 0
        if name[i] == "0":
            list0 = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 0 or col == 4) and (row != 0 and row != 6) or (row == 0 or row == 6) and (col > 0 and (col < 4)):
                        list0[row][col] = "*"
            lst1.append(list0)

        # 1
        elif name[i] == "1":
            list1 = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 2) or ((row == 6) and (col != 5)) or (row == 1 and col == 1) or (row == 2 and col == 0):
                        list1[row][col] = "*"
            lst1.append(list1)

        # 2
        elif name[i] == "2":
            list2 = [[" " for i in range(6)] for j in range(7)]
            i = 1
            j = 5
            for row in range(7):
                for col in range(6):
                    if (row == 6) or ((row == 0) and (col > 0 and col < 5)) or ((col == 0) and (row == 1)):
                        list2[row][col] = "*"
                    elif (row == i and col == j) and (row < 6):
                        i += 1
                        j -= 1
                        list2[row][col] = "*"
            lst1.append(list2)

        # 3
        elif name[i] == "3":
            list3 = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((row == 0 or row == 3 or row == 6) and (col > 0 and col < 4)) or ((col == 4) and (row != 0 and row != 3 and row != 6)):
                        list3[row][col] = "*"
            lst1.append(list3)

        # 4
        elif name[i] == "4":
            list4 = [[" " for i in range(6)] for j in range(7)]
            i = 1
            j = 3
            for row in range(7):
                for col in range(6):
                    if (row == 4 or col == 4):
                        list4[row][col] = "*"
                    elif (row == i and col == j):
                        i += 1
                        j -= 1
                        list4[row][col] = "*"
            lst1.append(list4)
            
        # 5
        elif name[i] == "5":
            list5 = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((row == 0) and (col != 5)) or (row == 3 or row == 6) and (col > 0 and col < 4) or (col == 4 and (row == 4 or row == 5))or (col == 0 and (row != 6 and row != 4)):
                        list5[row][col] = "*"
            lst1.append(list5)

        # 6
        elif name[i] == "6":
            list6 = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (row == 0 and col != 0 and col != 5) or (row == 3 or row == 6) and (col > 0 and col < 4) or (col == 4 and (row == 4 or row == 5))or (col == 0 and row > 0 and row < 6):
                        list6[row][col] = "*"
            lst1.append(list6)

        # 7
        elif name[i] == "7":
            list7 = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((row == 0 or col == 3) and (col < 4)) or ((row == 3) and (col == 2 or col == 4)):
                        list7[row][col] = "*"
            lst1.append(list7)

        # 8
        elif name[i] == "8":
            list8 = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((row == 0 or row == 3 or row == 6) and (col > 0 and col < 4)) or ((col == 0 or col == 4) and (row != 0 and row != 3 and row != 6)):
                        list8[row][col] = "*"
            lst1.append(list8)

        # 9
        elif name[i] == "9":
            list9 = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((row == 0 or row == 3 or row == 6) and (col > 0 and col < 4)) or (col == 4 and (row !=0 and row!=6)) or (col == 0 and (row == 1 or row == 2 or row == 5)):
                        list9[row][col] = "*"
            lst1.append(list9)


        else:
            print("Invalid")

    return lst1

name = input("Input any number : ")
lst2 = pattern()

for i in range(7):
    for j in range(len(lst2)):
        for k in range(6):
            print(lst2[j][i][k], end=" ")
        print(end="   ")
    print()
