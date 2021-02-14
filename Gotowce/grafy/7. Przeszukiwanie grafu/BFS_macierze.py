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
    Q.enqueue(vList[s])

    while not Q.is_empty():
        u = Q.dequeue()
        for i in range(n):
            v = vList[i]
            if G[u.index][v.index] == 1 and v.visited is False:     #wiem, ze G[u.index][i] tez by dizalalo, ale tak jest czytelniej ("Readability counts.")
                v.visited = True
                v.d = u.d + 1
                v.parent = u.index      #zwrocic uwage!!!
                Q.enqueue(v)
    return vList


def printBFS(G, i, vList):
    if vList[i].parent is None:
        print(vList[i].index)
        return
    printBFS(G, vList[i].parent, vList)
    print(vList[i].index)


G = [[0,1,1,0],[0,0,0,1],[0,1,0,1], [0,0,0,0]]
vList = BFS(G,0)
printBFS(G,3, vList)
