class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def switch(linkList, curr, prevCurr, aux, prevAux):
    prevCurr = curr.next    #"odpiecie" klucza

    if prevAux is None:     #przypisanie do poczatku listy
        linkList = curr
        linkList.next = aux
        curr = prevCurr.next
        return

    #przypisanie do srodka listy
    prevAux.next = curr     
    curr.next = aux
    curr = prevCurr.next    #wskaznik ustawiany na kolejy element

def insert(linkList, curr, prevCurr):
    aux = linkList
    prev = None
    while aux is not curr:
        if aux.val > curr.val:  #aux jest elementem ZA kluczem, prev elementem PRZED w posortowanej linkLiscie
            switch(linkList, curr, prevCurr, aux, prev) 
            return
        prev = aux
        aux = aux.next
    prevCurr = curr #jezeli klucz jest najwiekszym elementem, wystarczy iterowac wskaznik
    curr = curr.next

def insetSort(linkList):
    if linkList is None or linkList.next is None:
        return
    curr = linkList.next
    prev = linkList     #pierwszy element jest juz posortowany
    while curr is not None:
        insert(linkList, curr, prev)

def printLinkList(linkList):
    while linkList
        
