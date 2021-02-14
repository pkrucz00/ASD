from math import inf, sqrt


def dist(P1, P2):
    (x1, y1), (x2, y2) = P1, P2
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def separate(orderX, orderY, c, d):
    segX, segY = [], []
    for pointX in orderX:
        if pointX[0] >= c - d and pointX[0] <= c + d:
            segX.append(pointX)
    for pointY in orderY:
        if pointY[0] >= c - d and pointY[0] <= c + d:
            segY.append(pointY)
    return segX, segY


def shortSegmAux(orderX, orderY):
    n = len(orderX)
    if n <= 1:
        return inf, ("*****", "***")
    if n == 2:
        return dist(orderX[0], orderX[1]), (orderX[0], orderX[1])

    mid = n // 2
    c = orderX[mid][0]  # srodkowa linia

    dl, ansl = shortSegmAux(orderX[:mid], orderY[:mid])
    dr, ansr = shortSegmAux(orderX[mid:], orderY[mid:])
    if dl < dr:
        d, ans = dl, ansl
    else:
        d, ans = dr, ansr

    segX, segY = separate(orderX, orderY, c, d)
    for i in range(len(segY)):
        P1 = segY[i]
        for P2 in segY[i:i + 7]:
            if P1 != P2 and dist(P1, P2) < d:
                d = dist(P1, P2)
                ans = (P1, P2)

    return d, ans


def shortestSegment(P):
    orderX = sorted(P, key=lambda point: point[0])
    orderY = sorted(P, key=lambda point: point[1])

    return shortSegmAux(orderX, orderY)


d, answer = shortestSegment([(2, 2), (3, 3), (5, 5), (6, 5)])
print(f"Najkrótszy odcinek: {answer}\nDługość: {d}")
