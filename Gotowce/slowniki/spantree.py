from math import inf

class Node:
    def __init__(self, val, span):
        self.val = val
        self.span = span  #(a,b) - przedzial, za ktory odpowiada dany wezel
        self.intervals = []       #przedzialy zawarte w wezle
        self.left = None
        self.right = None

def spanTreeInit(data):
    def spanTreeAux(l, r, data):
        if len(data) == 0:
            return Node(None, (l,r))

        mid = len(data)//2
        root = Node(data[mid], (l,r))
        root.left = spanTreeAux(l, root.val, data[:mid])
        root.right = spanTreeAux(root.val, r, data[mid+1:])
        return root

    return spanTreeAux(-inf, inf, data)

def spanTreeInsert(root, interval):
    def spanTreeInsertAux(root, interval, aux):
        if root.span == aux:
            root.intervals.append(interval)
            return root
        else:
            a,b = root.span
            i,j= aux

            if a <= i and j <= root.val:
                root.left = spanTreeInsertAux(root.left, interval, (i, j))
            elif root.val <= i and j <= b:
                root.right = spanTreeInsertAux(root.right, interval, (i,j))
            else:
                root.left = spanTreeInsertAux(root.left, interval, (i, root.val))
                root.right = spanTreeInsertAux(root.right, interval, (root.val, j))
            return root

    return spanTreeInsertAux(root, interval, interval)

def printIntervals(root, val):
    if root.val is None:
        return root.intervals
    result = root.intervals[:]
    if val <= root.val:
        tmp = printIntervals(root.left, val)
    if val >= root.val:
        tmp = printIntervals(root.right, val)

    for inter in tmp:
        result.append(inter)
    return result

def removeInterval(root, interval):
    if root is not None:
        if interval in root.intervals:
            root.intervals.remove(interval)

        if root.val is None:
            return root

        i,j = interval
        a,b = root.span
        if a <= i and j <= root.val:
            root.left = removeInterval(root.left, interval)
        elif root.val <= i and j <= b:
            root.right = removeInterval(root.right, interval)
        else:
            root.left = removeInterval(root.left, interval)
            root.right = removeInterval(root.right, interval)
        return root



def prepareData(data):
    n = len(data)
    aux = [data[i][j] for i in range(n) for j in range(2)]
    aux.sort()
    result = [aux[0]]
    for i in range(1, 2*n):
        if aux[i] != aux[i-1]:
            result.append(aux[i])

    return result

data = [(0, 10), (5, 20), (7, 12), (10, 15)]
preparedData = prepareData(data)
T = spanTreeInit(preparedData)
for interval in data:
    T = spanTreeInsert(T, interval)
print(printIntervals(T, 10))