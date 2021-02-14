class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class PriorityQueue:
    def __init__(self, n):
        self.queue = [None]*n
        self.n = n
        self.len = 0

    def parent(self, i):
        return (i-1)//2
    def left(self, i):
        return 2*i+1
    def right(self, i):
        return 2*i+2

    def heapify(self, i):
        len = self.len
        left = self.left(i)
        right = self.right(i)
        smallest = i

        if left < len and self.queue[smallest].val > self.queue[left].val:
            smallest = left
        if right < len and self.queue[smallest].val > self.queue[right]. val:
            smallest = right

        if smallest != i:
            self.queue[i], self.queue[smallest] = self.queue[smallest], self.queue[i]
            self.heapify(smallest)

    def add(self, val):
        self.len += 1
        self.queue[self.len-1] = val

        i = self.len - 1
        while i > 0 and self.queue[self.parent(i)].val > self.queue[i].val:
            self.queue[i], self.queue[self.parent(i)] = self.queue[self.parent(i)], self.queue[i]
            i = self.parent(i)

    def get(self):
        if self.is_empty():
            raise Exception("***** ***")

        min = self.queue[0]
        self.len -= 1
        self.queue[0] = self.queue[self.len]
        self.heapify(0)

        return min

    def is_empty(self):
        return self.len == 0


def build_tree(A):
    Q = PriorityQueue(len(A))
    for elem in A:
        Q.add(Node(elem))


    for _ in range(len(A)-1):
        x = Q.get()
        y = Q.get()
        z = Node(x.val + y.val)
        z.left = y
        z.right = x
        Q.add(z)

    return z

def add_sum(T, h):
    if T.right is None and T.left is None:
        return T.val*h
    sum = 0
    if T.left is not None:
        sum += add_sum(T.left, h+1)
    if T.right is not None:
        sum += add_sum(T.right, h+1)
    return sum

def huffman_len(A):
    T = build_tree(A)
    sum = add_sum(T, 0)

    return sum




print(huffman_len([ 200, 700, 180, 120, 70, 30] ))
