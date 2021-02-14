'''
Paweł Kruczkiewicz, 401685

W zadaniu dane nie są równomiernie rozłożone, ponieważ są dane funkcją wykładniczą. Równo rozłożony jest jednak x
Najszybszym rozwiązaniem jest tutaj zastosowanie sortowania kubełkowego, jednakże potrzebne jest skorzystanie
z własności: "logarytm o podstawie a z a^x jest równy x" (z def logarytmu)

Pamiętać należy, że logarytmujemy JEDYNIE przy przypisaniu do kubeczków,
poszczególne dane w kubeczkach pozostają niezmienione.

Jeżeli do kubeczków trafiło więcej niż jeden element, to sortujemy je insertion sortem,
ponieważ jest on bardzo szybki dla małych ilości danych i sortuje w miejscu
oraz jest stabilny (w przypadku badań naukowych może to mieć znaczenie).

Złożoność algorytmu to O(n), ponieważ liniowo rozdysponowujemy elementy do kubeczków
(zakładamy, że operacja logarytmizowania jest O(1)),
sortowanie poszczególnych kubeczków jest O(1), ponieważ elementów w danym kubku jest O(1),
więc dla n kubeczków jest to koszt O(n);
scalanie również jest liniowe
Ostatecznie O(n) + O(n) + O(n) = O(n)

To oznacza, że posortowaliśmy całą tablicę w czasie liniowym
'''

from zad3testy import runtests
import math

def insertionSort(A):
    n = len(A)
    for j in range(1, n):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key

                 
    
def fast_sort(tab, a):
    n = len(tab)
    if n <= 1:
        return tab


    buckets = [ [] for _ in range(n+1) ]    #n+1 , ponieważ x może być równy 1
    for elem in tab:
        key = int(n*(math.log(elem, a)))    #korzystamy z logarytmowania dla znalezienia klucza
        buckets[key].append(elem)
    for bucket in buckets:
        insertionSort(bucket)       #sortujemy kubełki

    tab = []                        #resetujemy tablicę
    for bucket in buckets:          #łączymy kubełki
        tab += bucket


    return tab



runtests( fast_sort )
