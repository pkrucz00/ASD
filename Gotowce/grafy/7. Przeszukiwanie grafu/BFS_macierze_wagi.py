class Vertex:
    def __init__(self, index):
        self.index = index
        self.parent = None
        self.d = None
        self.visited = False

class Queue:
    def __init__(self, size):
        self.Q = [None]*size
        self.size = size
        self.elements = 0
        self.head = 0
    def enqueue(self, x):
        self.Q[(self.head + self.elements)%self.size] = x
        self.elements += 1    #bez operacji modulo, bo zarezerwujemy tyle pamieci, ze pelzajaca kolejka nie jest potrzebna
    def dequeue(self):
        tmp = self.Q[self.head]
        self.head = (self.head + 1) % self.size
        self.elements -= 1
        return tmp
    def is_empty(self):
        return self.elements == 0


def BFS(G, s):
    n = len(G)      #rzad grafu
    vList = [None]*n    #vertex list - lista wierzcholkow
    Q = Queue(n)     #kolejka
    for i in range(n):
        vList[i] = Vertex(i)   #inicjalizacja - vList przechowuje obiekty klasy vertex

    vList[s].visited = True
    vList[s].d = 0      #zmiana pola parent jest niepotrzebna (domysla wart klasy vertex)
    Q.enqueue((vList[s], 0, 0, None))

    while not Q.is_empty():
        u, x, d, parent = Q.dequeue()
        if x == 0:
            u.visited = True
            u.d = d
            u.parent = parent

            for i in range(n):
                v = vList[i]
                if G[u.index][v.index] is not None and v.visited is False:     #wiem, ze G[u.index][i] tez by dizalalo, ale tak jest czytelniej ("Readability counts.")
                    Q.enqueue((v,G[u.index][v.index]-1, d+1, u.index))

        else:
            if u.visited is False:
                Q.enqueue((u,x-1, d+1, parent))

    return vList


def printBFS(G, i, vList):
    if vList[i].parent is None:
        print(vList[i].index, end=" ")
        print(vList[i].d)
        return
    printBFS(G, vList[i].parent, vList)
    print(vList[i].index, vList[i].d)


G = [[None,2,1,None],
     [None,None,None,2]
    ,[None,2,None,5],
     [None,None,None,None]]
vList = BFS(G,0)
printBFS(G,3, vList)
