import functools
# otoczka wypukła

# wybór punktu najniższego, najbardziej po lewo
# funkcja zwraca wynik ujemny, 0 lub dodatni
def lower_cmp(p1, p2):
    return p1[1] - p2[1] if p1[1] != p2[1] else p1[0] - p2[0]

# iloczyn wektorowy
def cross_product(p1, p2):
    return p1[0] * p2[1] - p2[0] * p1[1]

# czy p2 jest bardziej na prawo od p1 względem układu z początkiem w miejscu x0?
# zwraca wynik ujemny (p2 na lewo), 0 (współliniowe) lub dodatni (p2 na prawo)
def clockwiseness(p0, p1, p2):
    p1 = (p1[0] - p0[0], p1[1] - p0[1])
    p2 = (p2[0] - p0[0], p2[1] - p0[1])
    return cross_product(p1, p2)

# komparator punktów względem p0
def angle_cmp(p0):
    def point_clockwiseness(p1, p2):
        return clockwiseness(p0, p1, p2)

    return point_clockwiseness

def graham(points):
    if len(points) < 4:
        return points

    lowest = min(points, key=functools.cmp_to_key(lower_cmp))
    ordered = sorted(points, key=functools.cmp_to_key(angle_cmp(lowest)))

    result = []
    result.append(ordered[0])
    result.append(ordered[1])

    for point in ordered[2:]:
        while clockwiseness(result[-2], result[-1], point) > 0:
            result.pop()
        result.append(point)

    return result

print(graham([(2,1), (3,3), (4,2.5), (5,4), (5,2), (6,1), (7,3)]))