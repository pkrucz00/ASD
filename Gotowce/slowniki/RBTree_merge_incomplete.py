BLACK = 1
RED = 0

class Node:
    def __init__(self, val):
       self.val = val
       self.color = BLACK
       self.parent = None
       self.left = None
       self.right = None

def floor_base_2(n):
    c = 2
    level = 1
    while c < n:
        c *= 2
        level += 1

    return c, level

def arrayToRBTree(arr, parent, left, right):
    if left > right:
        return None

    middle = (left+right) // 2
    T = Node(arr[middle])
    T.parent = parent
    T.left = arrayToRBTree(arr, left, middle - 1 )
    T.right = arrayToRBTree(arr, middle + 1, right)

    return T

def find_min(root):
    if root is None:
        return None

    while root.left is not None:
        root = root.left
    return root


def succ(root):
    if root is None:
        return None

    if root.right is not None:
        return find_min(root.right)
    else:
        while root.parent.left != root:
            root = root.parent
        return root.parent

def color(root,level, maxlevel):


def funkcja(T1, T2):    #T1, T2 - drzewa czerwono-czarne
    curr1 = find_min(T1)
    curr2 = find_min(T2)
    arr = []

    while curr1 != None and curr2 != None:
        if curr1.key < curr2.key:
            arr.append(curr1.key)
            curr1 = succ(curr1)
        elif curr1.key > curr2.key:
            arr.append(curr2.key)
            curr2 = succ(curr2)
        else:
            arr.append(curr2.key)
            curr1 = succ(curr1)
            curr2 = succ(curr2)
    while curr1 != None:
        arr.append(curr1.key)
        curr1 = succ(curr1)
    while curr2 != None:
        arr.append(curr2.key)
        curr2 = succ(curr2)

    T = arrayToRBTree(arr, None, 0, len(arr)-1)

    return T
