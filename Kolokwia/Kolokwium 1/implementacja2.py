Paweł Kruczkiewicz

Szukamy za pomoca funkcji select (o zlozonosci liniowej) indeksow wzrostu zolnierzy o wzroscie p i q. Nastepnie iterujemy tablice i dodajemy do tablicy wzrost wszystkich zolnierzy, ktorych wysokosc spelnia warunek p <= r <= q, gdzie r jest elementem tablicy.
Caly algorytm ma zlozonosc O(n) + O(n) = O(n)

def partition(A, p, r):
    i = p
    for j in range(p, r):
        if A[r] > A[j]:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i


def select(A, i, p, r):     #Oczekiwany czas O(n)
    if p == r:
        return A[r]
    q = partition(A, p, r)
    k = q-p+1
    if i == k:
        return A[q]
    elif i < k:
        return select(A, i, p, q-1)
    else:
        return select(A, i-k, q+1, r)

def section(T, p, q):
    T_copy = T[:]   #tworzymy kopię, aby nie zniszczyc wejsciowej tablicy (O(n)). Na koniec zbiera ja garbage collector
    p_value = select(T, p, 0, len(T)-1) #wartosc p-tego elementu
    q_value = select(T, q, 0, len(T)-1) #wartosc q-tego elementu

    acc = []        #akumulator
    for height in T_copy:   #O(n)
        if p_value <= height and height <= q_value:
            acc.append(height)      #dodanie do listy

    return acc

T = [160, 154, 176, 254,165,37,372, 276]
print(section(T, 3,7))