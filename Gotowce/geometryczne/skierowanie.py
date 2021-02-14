def crossproduct(p0, p1, p2):
    x1 = p1[0] - p0[0]
    x2 = p2[0] - p0[0]
    y1 = p1[1] - p0[1]
    y2 = p2[1] - p0[1]

    return x1*y2 - x2*y1


def is_clockwise(p0, p1, p2):
    return crossproduct(p0, p1, p2) > 0

def is_counterclockwise(p0, p1, p2):
    return crossproduct(p0, p1, p2) < 0


P0 = (0,0)
P = [(2,1), (1,2), (4,2)]

for i in range(len(P) - 1):
    for j in range(i+1,len(P)):
        if is_clockwise(P0, P[i], P[j]):
            print(f"{P[i]} is clockwise in regard to {P[j]}")
        elif is_counterclockwise(P0, P[i], P[j]):
            print(f"{P[i]} is counterclockwise in regard to {P[j]}")
        else:
            print(f"{P[i]} is collinear with {P[j]}")