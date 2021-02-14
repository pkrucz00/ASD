class Node:
    def __init__(self):
        self.val = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def printList(self):
        tmp = self.head
        while tmp:
            print(tmp.val)
            tmp = tmp.next
        print()

    def push(self, val):
        newNode = Node()
        newNode.val = val
        self.size += 1
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def push_back(self, val):
        newNode = Node()
        newNode.val = val
        self.size += 1
        if self.tail == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next

def merge(p, q, r):
    newl = LinkedList()
    qFix = q
    while p != qFix and q != r:
        if p.val < q.val:
            newl.push_back(p.val)
            p = p.next
        else:
            newl.push_back(q.val)
            q = q.next
    while p != qFix:
        newl.push_back(p.val)
        p = p.next
    while q != r:
        newl.push_back(q.val)
        q = q.next
    return newl

def MergeSort(lList):
    if lList.head == None or lList.head.next == None:  return lList
    if lList.size == 2:
        return merge(lList.head, lList.tail, None)

    p_prev = None
    p = lList.head
    q = p.next

    while True:
        q_prev = p
        while q != None and q_prev.val <= q.val:
            q_prev = q
            q = q.next
        if q == None:
            if p_prev == None:
                return lList
            else:
                p_prev = None
                p = lList.head
                q = p.next
                continue
        r_prev = q
        r = q.next
        while r != None and r_prev.val >= r.val:
            r_prev = r
            r = r.next

        sortedList = merge(p, q, r)

        if p_prev == None:
            lList.head = sortedList.head
        else:
            p_prev.next = sortedList.head
        sortedList.tail.next = r

        if r == None or r.next == None:
            p_prev = None
            p = lList.head
            q = p.next
        else:
            p_prev = r_prev
            p = r
            q = p.next



l = LinkedList()
l.push_back(3)
l.push_back(2)
l.push_back(6)
l.push_back(4)
l.push(2020)
l.push(2137)
l.printList()
sortedlist = MergeSort(l)
sortedlist.printList()