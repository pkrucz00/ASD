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
        self.Q[self.head + self.elements] = x
        self.elements += 1      #bez operacji modulo, bo zarezerwujemy tyle pamieci, ze pelzajaca kolejka nie jest potrzebna
    def dequeue(self):
        tmp = self.Q[self.head]
        self.head += 1          #bez modulo - wyjasnienie jak wyzej
        self.elements -= 1
        return tmp
    def is_empty(self):
        return self.elements == 0


def pathBFS(G, i, vList, path):
    if vList[i].parent is None:
        path.append(vList[i].index)
        return
    pathBFS(G, vList[i].parent, vList, path)
    path.append(vList[i].index)


def BFS(G, s, t):
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
            if G[u.index][v.index] > 0 and v.visited is False:     #wiem, ze G[u.index][i] tez by dizalalo, ale tak jest czytelniej ("Readability counts.")
                v.visited = True
                v.d = u.d + 1
                v.parent = u.index
                Q.enqueue(v)

    path = []
    pathBFS(G, t, vList, path)
    A = [(path[i], path[i+1]) for i in range(len(path)-1)]
    return A

def find_min(A, c):
    min = c[A[0][0]][A[0][1]]
    for u,v in A:
        if c[u][v] < min:
            min = c[u][v]
    return min

def make_gr(c, f):
    n = len(c)
    g_r = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if c[i][j] > 0:
                g_r[i][j] = c[i][j] - f[i][j]
            elif c[j][i] > 0:
                g_r[i][j] = f[j][i]
            else:
                g_r[i][j] = 0
    return g_r

def sumarize(f, s):
    n = len(f)
    sum = 0
    for i in range(n):
        sum += f[s][i]
    return sum

def max_flow(c, s, t):
    n = len(c)
    f = [[0 for _ in range(n)] for _ in range(n)]

    aug_p = BFS(c, s, t)
    while aug_p != []:
        min = find_min(aug_p, c)
        for u, v in aug_p:
            if c[u][v] > 0:
                f[u][v] += min
            else:
                f[v][u] -= min
        g_r = make_gr(c, f)
        aug_p = BFS(g_r, s, t)

    return sumarize(f, s)


c = [[0 for j in range(4)] for i in range(4)]
c[0][1] = 2
c[0][2] = 1
c[1][2] = 1
c[1][3] = 1
c[2][3] = 2
print(max_flow(c,0,3))
