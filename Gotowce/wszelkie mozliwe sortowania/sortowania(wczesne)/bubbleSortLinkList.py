import random

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def makeRandList(n):
    first = None
    for i in range(1, n+1):
        p = Node(random.randint(1,n))
        p.next = first
        first = p
    return p

def printList(head):
    aux = head
    while(aux is not None):
        print(aux.val)
        aux = aux.next
    print()
    
def Switch(prev, curr, nextEl):
    if prev is None:
        head = nextEl
        curr.next = nextEl
        head.next = curr
        return
    prev.next = nextEl
    curr.next = nextEl.next
    nextEl.next = curr

def listLength(head):
    counter = 0
    aux = head
    while(aux is not None):
        counter += 1
    return counter

def bubbleSort(head):
    if head is None or head.next is None:    return
    n = listLength(head)

    for i in range(n, 0, -1):
        curr = head
        prev = None
        print(curr.val)
        for j in range(i):
            if curr.val > curr.next.val:
                Switch(prev, curr, curr.next)
            prev = curr
            curr = curr.next

linkList = makeRandList(6)
printList(linkList)
bubbleSort(linkList)
printList(linkList)
