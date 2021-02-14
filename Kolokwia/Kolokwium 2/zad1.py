#Paweł Kruczkiewicz Zadanie 1

#dynamicznie: max_path(T) = max( max_path(S) + w(T,S)) po wszystkich synach roota drzewa T (w(T,S) to waga krawędzi łączącej z poddrzewem)
#dla roota naszego drzewa należy wybrać dwie najoptymalniejsze ścieżki (root może być
from math import inf

class Node:
    def __init__(self):
        self.children = 0
        self.child = []
        self.max_path = -inf
        self.good_son = None #syn, od którego otrzymalismy najlepszy wynik
        self.good_son_weight = None


def heavy_path_visit(T):
    if T.children == 0:
        return 0
    if T.max_path > 0:
        return T.max_path

    tmp = -inf
    for child, w in T.child:
        child_max_path = heavy_path_visit(child)
        if tmp < w + child_max_path:
            tmp = w + child_max_path
            T.good_son = child
            T.good_son_weight = w

    return tmp


def heavy_path(T):
    sum = 0
    sum += heavy_path_visit(T)
    T.child.remove((T.good_son, T.good_son_weight))
    sum += heavy_path_visit(T)

    return sum

A = Node()
B = Node()
C = Node()
A.children = 2
A.child = [ (B,5), (C,-1) ]
print(heavy_path(A))
