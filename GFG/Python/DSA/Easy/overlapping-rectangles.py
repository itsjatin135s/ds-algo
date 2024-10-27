# https://www.geeksforgeeks.org/problems/overlapping-rectangles1924/1


# Much much much better solution

class Solution:

    def do_overlap(self, L1, R1, L2, R2):
        # code here
        # If one rectangle is to the left of the other
        if L1[0] > R2[0] or L2[0] > R1[0]:
            return 0

        # If one rectangle is above the other
        if L1[1] < R2[1] or L2[1] < R1[1]:
            return 0

        # Otherwise, the rectangles overlap
        return 1


L1 = [72, -25]
R1 = [81, -61]
L2 = [24, -55]
R2 = [91, -60]


# worst solution can come up with hahaha

def doOverlap(L1, R1, L2, R2):
    # code here
    L3 = [L1[0], R1[1]]  # Left Bottom Of First Rectangle
    R3 = [R1[0], L1[1]]  # Right Top Of First Rectangle

    L4 = [L2[0], R2[1]]  # Left Bottom of Second Rectangle
    R4 = [R2[0], L2[1]]  # Right Top of Second Rectangle

    xMaxima = max(L1[0], R1[0])
    xMinima = min(L1[0], R1[0])

    yMaxima = max(L1[1], R1[1])
    yMinima = min(L1[1], R1[1])

    print(xMinima, xMaxima)
    print(yMinima, yMaxima)

    print(L2, R2)
    print(L4, R4)

    if (L2[0] in range(xMinima, xMaxima+1)) and (L2[1] in range(yMinima,
                                                                yMaxima+1)):
        print("here")
        return 1

    if (R2[0] in range(xMinima, xMaxima+1)) and (R2[1] in range(yMinima,
                                                                yMaxima+1)):
        print("here")
        return 1

    if (L4[0] in range(xMinima, xMaxima+1)) and (L4[1] in range(yMinima,
                                                                yMaxima+1)):
        print("here")
        return 1

    if (R4[0] in range(xMinima, xMaxima+1)) and (R4[1] in range(yMinima,
                                                                yMaxima+1)):
        print("here")
        return 1
   
    xMaxima = max(L2[0], R2[0])
    xMinima = min(L2[0], R2[0])

    yMaxima = max(L2[1], R2[1])
    yMinima = min(L2[1], R2[1])

    print("")
    print("-----------")
    print("-----------")
    print("-----------")
    print("")
    print(xMinima, xMaxima)
    print(yMinima, yMaxima)
    print(L1, R1)
    print(L3, R3)

    if (L1[0] in range(xMinima, xMaxima+1)) and (L1[1] in range(yMinima,
                                                                yMaxima+1)):
        print("here")
        return 1

    if (R1[0] in range(xMinima, xMaxima+1)) and (R1[1] in range(yMinima,
                                                                yMaxima+1)):
        print("here")
        return 1

    if (L3[0] in range(xMinima, xMaxima+1)) and (L3[1] in range(yMinima,
                                                                yMaxima+1)):
        print("here")
        return 1

    if (R3[0] in range(xMinima, xMaxima+1)) and (R3[1] in range(yMinima,
                                                                yMaxima+1)):
        print("here", R3[0], xMinima, xMaxima)
        return 1

    return 0


print(doOverlap(L1, R1, L2, R2))
