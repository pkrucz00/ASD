'''
Paweł Kruczkiewicz

Tworzymy drzewo przedziałowe (O(AlogA)) (A = |A|)
Dla i = {1...n}
Dodajemy przedział I[i] do drzewa przedziałowego
Wyszukujemy wszystkie przedziały, które przecinają punk ai (czyli lewą granicę naszego przedziału.
Z wyszukanych przedziałów znajdujemy ten najbardziej na lewo.
(de facto, gdy schodzimy po drzewie z góry na dół, to ten największy przecinający się, to ten, który byłby znaleziony pierwszy, ale nie mogę zmienić inplementacji drzewa przedziałoweg
Sprawdzamy jeszcze dla lewej granicy znalezionego lewego przedziału aż dojdziemy do końca drzewa przedziałowego bądź nie będzie więcej przedziałów. Złożoność: operacja intersect + insert, czyli O(k + log|A|) + O(log|A|) = O(k + log|A|)

Analogicznie postępujemy dla prawej strony, czyli prawego przedziału
Do tablicy z odpowiedziami na miejsce i wstawiamy wartość różnicy największego prawego przedziału z najmniejszego lewym przedziałem lub result[i-1] (w zaleznosci co jest większe)
Robimy tak aż dla każdego przedziału zawartego w I

Złożoność: O(logA + k)*|A| = O(|A|*(logA + k))
'''

from inttree import *

# przykladowy test uzycia drzewa przedzialowego 
# T = tree([1, 2, 3, 4, 5])
# tree_insert(T,(1, 4))
# tree_insert(T,(2, 5))
# tree_print(T)
# tree_remove(T,(1, 4))
# print()
# tree_print(T)
# tree_insert(T,(1, 3))
# print(tree_intersect(T, 3))
# exit(0)

def prepareData(data):
    n = len(data)
    aux = [data[i][j] for i in range(n) for j in range(2)]
    aux.sort()
    result = [aux[0]]
    for i in range(1, 2*n):
        if aux[i] != aux[i-1]:
            result.append(aux[i])

    return result

def find_min(arr):
    min = arr[0][0]
    for elem in arr:
        if elem[0] < min:
            min = elem[0]
    return min

def find_max(arr):
    max = arr[0][1]
    for elem in arr:
        if elem[1] > max:
            max = elem[1]
    return max

def intervals( I ):
    data = prepareData(I)   #tworzy posortowaną tablicę przedziałów elementarnych bez powtórzeń
    T = tree(data)

    result = []
    for elem in I:
        tree_insert(T, elem)
        intersecting = tree_intersect(T, elem[0])
        min_a = elem[0]
        while len(intersecting)  > 1:
            min_a = find_min(intersecting)
            intersecting = tree_intersect(T, min_a)

        intersecting_right = tree_intersect(T, elem[1])
        max_b = elem[1]
        while(len(intersecting_right) > 1):
            max_b = find_max(intersecting_right)
            intersecting_right = tree_intersect(T, max_b)

        i = I.index(elem)
        if i == 0:
            result.append(max_b - min_a)
        else:
            result.append(max(max_b - min_a, result[i-1]))

    return result





# uruchamia bazowe testy uzywajac funkcji intervals do obliczania wyniku
# wypisuje na koncu "OK!" jesli testy zaliczone
run_tests(intervals)





