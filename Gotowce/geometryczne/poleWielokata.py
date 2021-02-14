def trapezoidArea(y0, P1, P2):
    (x1, y1) = P1
    (x2, y2) = P2
    a = y1 - y0
    b = y2 - y0
    h = abs(x2 - x1)
    return (a+b)*h/2

def find_base(P):
    q = sorted(P, key=lambda point: point[1])
    return q[0][1]          #zwraca najmniejszą wysokość

def computeArea(P):
    areaSum = 0
    n = len(P)
    y0 = find_base(P)

    for i in range(n):
        nextind = (i+1)%n
        if P[nextind][0] < P[i][0]:
            areaSum += trapezoidArea(y0, P[i], P[nextind])
        else:
            areaSum -= trapezoidArea(y0, P[i], P[nextind])

    return areaSum


P = [(1,2), (4,-2), (6,1), (7,4), (5,8), (2,4)]
print(computeArea(P))
