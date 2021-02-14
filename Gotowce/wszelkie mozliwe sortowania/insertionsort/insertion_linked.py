class Node:
    def __init__(self):
        self.val = None
        self.next = None

def insertionLinked(head):
    if head == None or head.next == None:
        return head

    prev_key = head
    key = head.next
    while key != None:
        cur_prev = None
        cur = head
        while cur != key and cur.val <= key.val:
            cur_prev = cur
            cur = cur.next
        if cur.val > key.val:
            prev_key.next = key.next
            if cur_prev == None:
                head = key
                head.next = cur
            else:
                cur_prev.next = key
                key.next = cur
            key = prev_key.next
        else:
            prev_key = key
            key = key.next
    return head

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
    print()

head = Node()
head.val = 1
head = push(head, 4)
head = push(head, 2)
head = push(head, 3)
head = push(head, 8)
printNode(head)
head = insertionLinked(head)
printNode(head)
