class BSTNode:
    def __init__(self):
        self.key = None
        self.val = None
        self.parent = None
        self.left = None
        self.right = None

def find(root, key):
    while root is not None:
        if root.key == key:
            return root
        elif root.key < key:
            root = root.right
        else:
            root = root.left
    return None

def insert(root, key, val):
    if root is None:
        root = BSTNode()
        root.key = key
        root.val = val
        return root

    prev = None
    iter = root
    while iter is not None:
        if iter.key < key:
            prev = iter
            iter = iter.right
        else:
            prev = iter
            iter = iter.left


    iter = BSTNode()
    iter.key = key
    iter.val = val
    iter.parent = prev
    if prev.key > iter.key:
        prev.left = iter
    else:
        prev.right = iter

    return root


def find_min(root):
    if root is None:
        return None

    while root.left is not None:
        root = root.left
    return root

def find_max(root):
    if root is None:
        return None

    while root.right is not None:
        root = root.right
    return root

def printing(root):
    if root is not None:
        printing(root.left)
        print(root.val)
        printing(root.right)

def succ(root):
    if root is None:
        return None

    if root.right is not None:
        return find_min(root.right)
    else:
        while root.parent.left != root:
            root = root.parent
        return root.parent

def prev(root):
    if root is None:
        return None

    if root.left is not None:
        return find_max(root.left)
    else:
        while root.parent.right != root:
            root = root.parent
        return root.parent

def remove(root, key):
    if root is None:
        return None

    if key < root.key:
        root.left = remove(root.left, key)
    elif key > root.key:
        root.right = remove(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            tmp = succ(root.right)
            root.val = tmp.val
            root.key = tmp.key
            root.right = remove(root.right, key)

    return root



T = insert(None, 4, "Świnia")
T = insert(T, 3, "Kurwa")
T = insert(T, 7, "Pies")
T = insert(T, 2, "Gdynia")
T = insert(T, 6, "ją")
T = insert(T, 5, "Jebał")
T = insert(T, 1, "Arka")

printing(T)
print()

T = remove(T, 7)
T = remove(T, 6)
T = remove(T, 5)

printing(T)