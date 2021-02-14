class Node:
    
    def __init__(self):
        self.val = None
        self.next = None

class LinkedList:  
    def __init__(self):
        self.head=None
    def printList(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp=temp.next
    def push(self,val):
        newNode=Node()
        newNode.val = val
        if (self.head==None):
            self.head=newNode
        else:
            newNode.next = self.head
            self.head = newNode
    def QuickSort(self):
        self.head=QuickSortRecur(self.head, gettail(self.head))
    

def gettail(head):
    temp=head
    prev=None
    while temp:
        prev=temp
        temp=temp.next
    return prev

def partition(head, end, newHead, newEnd):
    pivot=end
    prev=None
    cur=head
    tail=pivot
    
    while (cur!=pivot):
        if cur.val < pivot.val:
            if newHead==None:
                newHead=cur
            prev=cur
            cur=cur.next
        else:
            if prev!=None:
                prev.next=cur.next
            tmp=cur.next
            cur.next=None
            tail.next=cur
            tail=cur
            cur=tmp
    if newHead==None:
        newHead=pivot
    newEnd=tail
    
    return pivot, newHead, newEnd

def QuickSortRecur (head, end):
    if head==None or head==end:
        return head
    
    newHead=None
    newEnd=None
    
    pivot,newHead,newEnd = partition(head,end, newHead, newEnd)
    
    if newHead!=pivot:
        tmp=newHead
        while(tmp.next!=pivot):
            tmp=tmp.next
        tmp.next=None
        
        newHead=QuickSortRecur(newHead, tmp)
        
        tmp=gettail(newHead)
        tmp.next=pivot
    
    pivot.next=QuickSortRecur(pivot.next,newEnd)
    
    return newHead



if __name__=='__main__':
    llist=LinkedList()
    llist.push(7)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    llist.push(6)
    llist.QuickSort()
    llist.printList()