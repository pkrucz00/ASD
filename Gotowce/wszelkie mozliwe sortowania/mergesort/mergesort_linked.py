#mergesort na linkedlistach

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def getSize(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


def merge(head1, head2):
    if head1.val < head2.val:
        newHead = head1
        head1 = head1.next
    else:
        newHead = head2
        head2 = head2.next

    iter = newHead
    while head1 is not None and head2 is not None:
        if head1.val < head2.val:
            iter.next = head1
            head1 = head1.next
        else:
            iter.next = head2
            head2 = head2.next
        iter = iter.next

    if head1 is not None:
        iter.next = head1
    if head2 is not None:
        iter.next = head2

    return newHead


def mergeSort(head):
    if head is None:
        return None
    if head.next is None:
        return head

    prev = None
    iter = head

    size = getSize(head)
    for _ in range(size//2):
        prev = iter
        iter = iter.next

    prev.next = None

    head1 = mergeSort(head)
    head2 = mergeSort(iter)

    head = merge(head1, head2)

    return head

def printList(head):
    while head is not None:
        print(head.val)
        head = head.next
    print()


head = Node(5)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(7)
printList(mergeSort(head))