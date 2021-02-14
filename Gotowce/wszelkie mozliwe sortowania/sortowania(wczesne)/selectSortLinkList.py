import random

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def makeList(n):
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

def changeLinks(head, prevCurr, curr, prevSelected, selected):
    if prevCurr is None:
        head = selected
        currNext = curr.next
        prevSelected.next = curr
        curr.next = selected.next
        selected.next = currNext
    else:
        currNext = curr.next
        prev.next = selected
        prevSelected.next = curr
        curr.next = selected.next
        selected.next = currNext
    curr = selected.next
    prev = selected

def selectSort(head):
    if head is None or head.next is None:    return
    curr = head
    prevCurr = None
    while curr is not None:
        i = curr
        prev_i = None
        minimal = curr
        prev_minimal = None
        
        while i is not None:
            if i.val > minimal.val:
                minimal = i
                prev_minimal = prev_i
            i = i.next
        changeLinks(head, prevCurr, curr, prev_minimal, minimal)

if __name__ == "__main__":
    p = makeList(6)
    printList(p)
    selectSort(p)
    printList(p)
