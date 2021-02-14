'''
Paweł Kruczkiewicz, 401685

To zadanie jest bardzo podobne do zadania "kosztowne krawędzie" omawianego na wykładzie.
W algorytmie korzystamy ze zmodyfikowanej wersji algorytmu BFS,
która w miejsce wierzchołka o wadze n tworzy n-1 sztucznych "wierzchołków".
W tym zadaniu użycie takiego algorytmu jest umotywowane właśnie
1) wagami zawartymi w zbiorze liczb naturalnych
2) górnym ograniczeniem wagi (w tym przypadku 8),
 dzięki któremu złożoność asymptotyczna algorytmu nie wzrasta w stosunku do standardowego BFSa

Dodatkowo należy do kolejki dodawać informację o rodzicu, ponieważ wtedy wiemy,
jaki był koszt poprzedniej drogi i jednocześnie możemy ją ominąć

Jako dodatkowa optymalizacja możemy zaprzestać przeszukiwanie wszerz, gdy wierzchołek B zostanie odwiedzony.
Nie zmienia to asymptotycznego czasu wykonywania algorytmu, jednakże w rzeczywistości nieco go przyśpiesza.

Złożoność algorytmu to O(c*(V+E)), gdzie c to górne ograniczenie na koszt krawędzi.
Ponieważ mamy do czynienia z macierzową reprezentacją grafu, to dla V = O(n), wyszukiwanie krawędzi zajmuje czas O(n^2)
Zatem ostateczna złożoność algorytmu to O(c*n^2) = O(n^2) (z definicji notacji dużego O) dla V = n

'''


from zad1testy import runtests
from queue import Queue # korzystamy z kolejki wbudowanej. Dozwolone (punkt 1 w pliku main.pdf)

class Vertex:                   # klasa na wierzchołek
    def __init__(self, index):
        self.index = index
        self.parent = None      # W polu parent znajduje się jedynie INDEKS wierzchołka, nie klasa
        self.d = None
        self.visited = False


def should_visit(G, u, v, parent):   # sprawdzenie, czy dany wierzchołek "v" jest osiągalny z przetworzonego "u"
    if parent is None:
        return G[u.index][v.index] > 0 and v.visited is False
    else:
        return G[u.index][v.index] > 0 and v.visited is False\
               and G[u.index][v.index] != G[u.parent][u.index]


def islands(G, A, B):
    n = len(G)
    vList = [None]*n    # vertexList - lista wierzchołków
    Q = Queue()         # kolejka bez górnej granicy
    for i in range(n):
        vList[i] = Vertex(i)        # uzupełnienie tablicy z informacjami dla wierzchołków

    vList[A].visited = True         # przetworzenie pierwszego wierzchoka
    vList[A].d = 0
    Q.put((vList[A], 0, 0, None))      # krotki z informacją (wierzchołek, waga, odległość, rodzic)

    while not Q.empty():
        u, x, d, parent = Q.get()       #wyciągnięcie informacji z kolejki
        if x == 0:
            u.visited = True        #przetworzenie wierzchołka
            u.d = d
            u.parent = parent

            if u.index == B:        #delikatna optymalizacja
                return u.d

            for i in range(n):
                v = vList[i]
                if should_visit(G, u, v, parent):
                    Q.put((v, G[u.index][v.index]-1, d+1, u.index))

        else:
            if u.visited is False:
                Q.put((u, x-1, d+1, parent))    #dodajemy sztuczny wierzchołek

    return None #jeżeli wykonaliśmy BFS dla wierzchołka A, a wierzchołka B nie znaleźliśmy, to znaczy, że nie jest on osiągalny
        

runtests( islands ) 
