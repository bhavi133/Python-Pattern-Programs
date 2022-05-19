def pattern():

    for i in range(len(name)):

        # A
        if name[i] == "A":
            listA = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((col == 0 or col == 5) and (row != 0)) or (row == 0 or row == 3) and (col > 0 and col < 5):
                        listA[row][col] = "*"
            list1.append(listA)

        # B
        elif name[i] == "B":
            listB = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 0) or (col == 4 and (row != 0 and row != 3 and row != 6)) or ((row == 0 or row == 3 or row == 6) and (col > 0 and col < 4)):
                        listB[row][col] = "*"
            list1.append(listB)

        # C
        elif name[i] == "C":
            listC = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 0) and (row != 0 and row != 6) or (row == 0 or row == 6) and (col > 0):
                        listC[row][col] = "*"
            list1.append(listC)

        # D
        elif name[i] == "D":
            listD = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((col == 0) or (col == 5) and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (col > 0 and col < 5)):
                        listD[row][col] = "*"
            list1.append(listD)

        # E
        elif name[i] == "E":
            listE = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 0) or (row == 0 or row == 3 or row == 6) and (col > 0):
                        listE[row][col] = "*"
            list1.append(listE)

        # F
        elif name[i] == "F":
            listF = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 0) or (row == 0 or row == 3) and (col > 0):
                        listF[row][col] = "*"
            list1.append(listF)

        # G
        elif name[i] == "G":
            listG = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((row == 0 or row == 6) and (col != 5)) or (col == 0 or col == 4 and (row > 2)) or (row == 3) and (col > 2):
                        listG[row][col] = "*"
            list1.append(listG)

        # H
        elif name[i] == "H":
            listH = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 0 or col == 5) or (row == 3) and (col > 0 and col < 5):
                        listH[row][col] = "*"
            list1.append(listH)

        # I
        elif name[i] == "I":
            listI = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((row == 0 or row == 6) and (col != 5)) or (col == 2):
                        listI[row][col] = "*"
            list1.append(listI)

        # J
        elif name[i] == "J":
            listJ = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 2) or ((row == 0) and (col != 5)) or (row == 6 and (col < 2)):
                        listJ[row][col] = "*"
            list1.append(listJ)
