Paweł Kruczkiewicz

Bierzemy kazda z liczb, liczymy dla kazdej indeks jedno- i wielokrotnych cyfr. Nastepnie dwa razy przeprowadzamy counting sort (bo liczby sa calkowite od 0 do 9), pierwszy raz po wielokrotnych, drugi raz po jednokrotnych. Na koniec przepisujemy klucze, czyli pierwsze wartosci z tupli, do wyjsciowej tablicy:
Zlozonosc algorytmu: O(n) (niemal kazdy krok jest liniowy, zakladamy, ze wielkosc liczb jest znacznie mniejsza od wielkosci tablicy)



def getMax(A,i):
    maximum = 0
    for elem in A:
        if elem[i] > maximum:
            maximum = elem[i]
    return maximum


def countingSort(A, index):     #index mowi czy sortujemy po wielokrotnych, czy jednokrotnych
    n = len(A)
    result = [0] * n
    k = getMax(A, i)
    aux = [0] * k

    for i in range(n):
        aux[A[i][index]] += 1
    for i in range(1, k):
        aux[i] += aux[i-1]
    for i in range(n-1, -1, -1):
        result[aux[A[i][index]]-1] = A[i]
        aux[A[i][index]] -= 1

        for i in range(n):
            A[i] = result[n-1-i]      #przepisujemy tablice "na odwrót, aby porządek był malejący

    return A


def pretty_index(elem):
    digits = [0]*10
    aux = elem
    while aux > 0:
        tmp = aux % 10
        digits[tmp] += 1
        aux = aux//10
    wielokrotne = jednokrotne = 0
    for digit in digits:
        if digit == 1:
            jednokrotne += 1
        elif digit >= 1:
            wielokrotne += 1
    return (elem, jednokrotne, wielokrotne)



def pretty_sort(T):
    n = len(T)
    pretty_list = []
    for number in T:    #O(n)
        pretty_list.append(pretty_index(number))    #tworzymy tablice z iformacjami o liczbie czyli ile ma jedno- i wielokrotnych cyfr

    pretty_list = countingSort(pretty_list, 2)  #sortujemy wg wielokrotnych  (O(n))
    pretty_list = countingSort(pretty_list, 1)  #sortujemy wg jednokrotnych

    result = []
    for i in range(n):
        result.append(pretty_list[i][0])        #przepisujemy jedynie klucz danej krotki
    return result

#caly algorytm: zlozonosc O(n)