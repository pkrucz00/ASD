from math import sqrt

def det3x3(a,b,c):
    s1 = a[0]*b[1] + b[0]*c[1] + c[0]*a[1]
    s2 = a[1]*b[0] + b[1]*c[0] + c[1]*a[0]
    return s1 - s2

def divide(a,b,c):
    eps = 10**(-14)

    det = det3x3(a, b, c)   # computing the determinant of given interval and the point c
    if det < -eps:           # c is clockwise to the interval - it's on its right 
        return -1
    elif det > eps:          # c is counterclockwise to the interval - it's on its left
        return 1
    else:                    # c is within the "epsilon range" - collinear
        return 0

def partition(P, start, stop, p0):
    i = start
    for j in range(start, stop):
        if divide(p0, P[stop], P[j]) < 0:
            P[i],P[j]=P[j],P[i]
            i += 1
    P[stop],P[i] = P[i], P[stop]
    return i

def quickSort(P, start, stop, p0):
    if start < stop:
        pivot = partition(P, start, stop, p0)
        quickSort(P, start, pivot - 1, p0)
        quickSort(P, pivot + 1, stop, p0)

def intervalLength(a,b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def removeShorter(P, a,b, p0):
    if intervalLength(a, p0) < intervalLength(b, p0):
        P.remove(a)
    else:
        P.remove(b)   

def removeCollinear(P, p0):
    n = len(P)
    i = 0
    for _ in range(n-1):
        if divide(p0, P[i], P[i+1]) == 0:
            removeShorter(P, P[i], P[i+1], p0)
        else:
            i += 1
            
def findp0(P):
    Arr = sorted(P, key= lambda point: point[1])
    Arr = sorted(Arr, key= lambda point: point[0])
    return Arr[0]


def Graham(P):
    p0 = findp0(P)

    Pcopy = P[:]
    Pcopy.remove(p0)
    quickSort(Pcopy, 0, len(sortedPoints) - 1, p0)
    removeCollinear(Pcopy, p0)

    stack = [p0, Pcopy[0], Pcopy[1]]

    for point in pCopy[2:]:
        P1, P2 = stack[-2], stack[-1]
        while is_counterclockwise(P1, P2, point):
            stack.pop()
            P1, P2 = stack[-2], stack[-1]
        stack.append(point)

    return stack


print(Graham([(2,1), (3,3), (4,2), (5,4), (5,2), (6,1), (7,3)]))




