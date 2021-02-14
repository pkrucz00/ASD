class Node:
    def __init__(self):
        self.val = None
        self.next = None


def push(head, newVal):
    newEl = Node()
    newEl.val = newVal
    newEl.next = head
    head = newEl
    return head

def printNode(head):
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next

def getTail(head):
    curr = head
    while curr is not None and curr.next is not None:
        curr = curr.next
    return curr

def partitionLinked(head, tail):
    pivot = tail
    prev = None
    cur = head
    last = pivot
    newHead = None

    while cur != pivot:
        if cur.val < pivot.val:
            if newHead == None:
                newHead = cur
            prev = cur
            cur = cur.next
        else:
            if prev != None:
                prev.next = cur.next
            tmp = cur.next
            cur.next = None
            last.next = cur
            last = cur
            cur = tmp

    if newHead == None:
        newHead = pivot

    newTail = last
    return pivot, newHead, newTail

def quickSortLinked(head, tail):
    if head == None or head.next == None:
        return head

    pivot, newHead, newTail = partitionLinked(head, tail)
    if newHead != pivot:
        tmp = newHead
        while tmp.next != pivot:
            tmp = tmp.next
        tmp.next = None

        newHead =quickSortLinked(newHead, tmp)

        tmp = getTail(newHead)
        tmp.next = pivot

    pivot.next = quickSortLinked(pivot.next, newTail)

    return newHead

head = Node()
head.val = 1
head = push(head, 4)
head = push(head, 2)
head = push(head, 3)
printNode(head)
tail = getTail(head)

head = quickSortLinked(head, tail)
print()
printNode(head)
