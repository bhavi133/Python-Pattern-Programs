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
            
        # K
        elif name[i] == "K":
            listK = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 0 or row + col == 3 or row - col == 3):
                        listK[row][col] = "*"
            list1.append(listK)

        # L
        elif name[i] == "L":
            listL = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 0) or (row == 6) and (col > 0):
                        listL[row][col] = "*"
            list1.append(listL)

        # M
        elif name[i] == "M":
            listM = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 0 or col == 4) or (row == col) and (col < 3) or (col+row == 4 and row != 3):
                        listM[row][col] = "*"
            list1.append(listM)
            
        # N
        elif name[i] == "N":
            listN = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 0 or col == 5) or (row == col):
                        listN[row][col] = "*"
            list1.append(listN)

        # O
        elif name[i] == "O":
            listO = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 0 or col == 5) and (row > 0 and row < 6) or (row == 0 or row == 6) and (col != 0 and col != 5):
                        listO[row][col] = "*"
            list1.append(listO)

        # P
        elif name[i] == "P":
            listP = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((col == 0) or (col == 5) and (row > 0 and row < 3)) or (row == 0 or row == 3) and (col != 5):
                        listP[row][col] = "*"
            list1.append(listP)

        # Q
        elif name[i] == "Q":
            listQ = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 0 or col == 5) and (row != 0 and row != 5 and row != 6) or (row == 0 or row == 5) and (col > 0 and col < 5) or (row == 4 or col == 2) and (col > 1 and col < 3 and row > 3 and row < 5) or (col == 3 and row == 6):
                        listQ[row][col] = "*"
            list1.append(listQ)

        # R
        elif name[i] == "R":
            listR = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 0) or ((col == 4) and (row == 1 or row == 2 or row == 6)) or ((row == 0 or row == 3) and (col > 0 and col < 4)) or (col == 2 and row == 4) or (col == 3 and row == 5) or (col == 4 and row == 6):
                        listR[row][col] = "*"
            list1.append(listR)

        # S
        elif name[i] == "S":
            listS = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((row == 0 or row == 3 or row == 6) and (col != 0 and col != 5)) or ((col == 0) and (row > 0 and row < 3)) or ((col == 5) and (row > 3 and row < 6)):
                        listS[row][col] = "*"
            list1.append(listS)

        # T
        elif name[i] == "T":
            listT = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 2) or ((row == 0) and (col != 5)):
                        listT[row][col] = "*"
            list1.append(listT)

        # U
        elif name[i] == "U":
            listU = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 0 or col == 5) and (row != 6) or (row == 6) and (col > 0 and col < 5):
                        listU[row][col] = "*"
            list1.append(listU)

        # V
        elif name[i] == "V":
            listV = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((col == 0 or col == 4) and (row < 5)) or ((row == 5) and (col == 1 or col == 3)) or (row == 6 and col == 2):
                        listV[row][col] = "*"
            list1.append(listV)

        # W
        elif name[i] == "W":
            listW = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 0 or col == 4) or (col == 2 and row == 4) or (row == 5 and col == 1) or (row == 5 and col == 3):
                        listW[row][col] = "*"
            list1.append(listW)

        # X
        elif name[i] == "X":
            listX = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col == 0 or col == 4) and ((row != 2 and row != 3 and row != 4)) or ((row == 2 or row == 4) and (col == 1 or col == 3)) or (col == 2 and row == 3):
                        listX[row][col] = "*"
            list1.append(listX)

        # Y
        elif name[i] == "Y":
            listY = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (row == col) and (row < 3) or (col == 2) and (row > 2) or (col == 4 and row == 0) or (col == 3 and row == 1):
                        listY[row][col] = "*"
            list1.append(listY)

        # Z
        elif name[i] == "Z":
            listZ = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if (row == 0 or row == 6) or (row + col == 5):
                        listZ[row][col] = "*"
            list1.append(listZ)

        else:
            print("Invalid")

    return list1

name = input("Input a name : ")
list1 = []
list2 = pattern()

for i in range(7):
    for j in range(len(list2)):
        for k in range(6):
            print(list2[j][i][k], end=" ")
        print(end="   ")
    print()
