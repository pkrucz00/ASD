'''
Paweł Kruczkiewicz

Problemem przy wykasowaniu jednego klucza z tablicy z haszowaniem z adresowaniem otwartym jest przerwany ciąg liczb o tym samym kluczu.
Element o kluczu k1 mogł zostać wstawiony w miejsce T[k1+c], gdzie w bardzo pesymistycznym przypadku (bardzo bardzo pesymistycznym) c jest niemal równe bądź równe n
Tym samym naiwne rozwiązanie, czyli próba wyszukania wszystkich wstawionych wcześniej kluczy odbyłaby się w pesymistycznym czasie O(n^2), bo każdy element mógł być wyszukiwany w czasie n.
W tym naiwnym rozwiązaniu program naprawiłby to miejsce, w którym napotkał "dziurę" czyli None
Niestety, nie mam pomysłu na  lepsze rozwiązanie niż powyższe, więc zabiorę się implementację tego zazwyczaj liniowego, ale jednak możliwie kwadratowego rozwiązania.
Swoje próby znalezienia odpowiedzi lepszej zostawiam poniżej, bo może coś mądrego tam jednak dopisałem. To taka bardziej informacja dla mnie, jak blisko byłem właściwego rozwiązania.

Złożoność: Dla wyszukiwania w czasie O(1): O(N)
            Dla wyszukiwania w czasie O(N): O(N) * O(N) = O(N^2) - przy dobrej funkcji haszującej i odpowiednim powiększaniu tablicy z haszowaniem przy dużym współczynniku przepełnienia - prawie znikome prawdopodobieństwo)

[Poniżej znajdują się próby znalezienia innego sposobu rozwiązania tego zadania. Zachowane w celach archiwalnych - chcę wiedzieć, jak wiele nie wiem]

Dlatego należy zauważyć, ze przejście po każdym indeksie tablicy z haszowaniem jest liniowe. Jeżeli znajdziemy sposób na upewnienie się, że dany element jest osiągalny w czasie O(1), to mamy rozwiązanie zawsze liniowe.
Jak to zrobić?
Przechodzimy po tablicy z haszowaniem.
Liczymy hasz pierwszego elementu. Jeżeli zgadza się z jego indeksem, lecimy dalej, jeśli nie, to przechodzimy do wyznaczonego przez hasz indeksu i staramy się przeskoczyć do naszego elementu. Zapamiętujemy ten "idealny hasz"
Jeżeli po drodze napotkamy pole z taken=False, to nastawiamy je na True, bo to jest miejsce zniszczone w wyniku ataku komputerowego. (Złożoność tego kroku: pesymistycznie O(N))

Przechodzimy do kolejnego elementu. Jeżeli hasz zgadza się z poprzednim elementem, przechodzimy dalej.
Jeżeli hasz zgadza się z indeksem (czyli element trafił na swoje miejsce bez konfliktu) również przechodzimy dalej.
Jeżeli hasz się nie zgadza ani z idealnym haszem ani z indeksem, to sprawdzamy, czy hasz trafił między idealny hasz a iterowany element.
Jeśli trafił, to idziemy dalej, jeśli nie, to znaczy, że klucz pozwalający na dotarcie do tego elementu został skasowany gdzieś dalej, więc go zapamiętujemy.
Jeżeli napotkamy None

'''


class Node:
    def __init__(self, key = None, taken = False):
        self.key = key
        self.taken = taken
        
    def __str__(self):
        if not self.taken:
            print('pusty')
        else:
            print('klucz: ', self.key)


def h(key):
    v = int('0b10101010', 2)
    for l in key:
        v ^= ord(l) % 255
    
    return v % N


N=11
hash_tab = [Node() for i in range(N)]


def find(hash_tab, key):        #przekopiowałem tutaj, ponieważ funkcja recover nie działała bez tego. Mam nadzieję, ze to nie grzech.
    idx = h(key)
    for i in range(N):
        if not hash_tab[idx].taken: return None
        if hash_tab[idx].key == key: return idx
        idx = (idx + 1) % N

    return None


def recover_aux(hash_tab, key):
    idx = h(key)
    for i in range(N):
        if not hash_tab[idx].taken:
            hash_tab[idx].taken = True
            return hash_tab
        idx = (idx + 1) % N


def recover(hash_tab):
    for elem in hash_tab:
        if elem.key is None:
            continue
        if find(hash_tab, elem.key) is None:
            return recover_aux(hash_tab, elem.key)
        else:
            pass
