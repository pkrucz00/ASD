'''
Paweł Kruczkiewicz 401685

Jest to przykład algorytmu zachłannego.
Dla każdego ciągu liczb szukamy najmniejszej wartości tymczasowej, wybieramy ją, dodajemy elementy i powtarzamy proces
aż do uzyskania wyniku końcowego. Zapamiętujemy największą z obliczonych wartości tymczasowych (tj. bierzemy max).

Przeszukiwanie tablicy w celu znalezienia najmniejszej wartości tymczasowej zajmuje O(n)
Rekurencja ma głębokość O(n)
Zatem złożoność algorytmu to O(n)*O(n) = O(n^2)

Algorytm działa zachłannie, ponieważ wybieramy wynik lokalnie najlepszy.
Aby pokazać, że algorytm jest poprawny, udowodnijmy najpierw jego słuszność dla k = 3
Zakładamy BSO, że idealne dodawanie to n1+n2, a dopiero potem (n1+n2)+n3
Nasz algorytm wybiera n2+n3, a później n1+(n2+n3)
Zakładamy również, że abs(n1+n2) >= abs(n2+n3) (przez sprzeczność)

Zauważamy, że największą wartością tymczasową może tutaj być jedynie jeden z wybranych wyników.
Jeżeli to końcowy jest największy, to nasz algorytm spisał się tak samo dobrze jak wzorcowy, bo dodawanie jest przemienne
( tj. n1 + n2= n3 = (n1 + n2) + n3 = n1 + n2 + n3) )
Jeżeli z kolei to pierwszy wynik tymczasowy jest większy od drugiego, to z założenia widzimy,
że wybraliśmy mniejszą bądź równą wartość w porównaniu z tą wzorcową,
więc nasz algorytm pokazuje rozwiązanie niegorsze od wzorcowego, czyli jest poprawny.

Rozszerzamy to do 4 elementów
Jeżeli maksymalna wartość tymczasowa nie jest wartością końcową ani nie sumuje elementu 4, to nasz algorytm działa poprawnie,
co udowodniono wyżej (założenie indukcyjne)
Jeżeli maksymalna wartość tymczasowa zawiera składnik n4, to nasz algorytm w którymś zejściu rekurencyjnym wskaże tę wartość.
Zakładamy, że się pomylił. Wtedy istnieje rozwiązanie różne od wskazanego przez algorytm. Jak się jednak okazuje, we wzorcowym
rozwiązaniu, w pewnym momencie wystąpiłaby wartość tymczasowa większa lub równa od wybranej (ze względu na przemienność dodawania).
Nie może być większa, bo to byłaby sprzeczność, może być co najwyżej równa.
W tym wypadku nasz algorytm wskazał niegorszą odpowiedź od wzorowej.

Podobnie można uogólnić rozumowanie do k-składnikowej sumy. Zatem algorytm zachłanny jest poprawny dla k liczb naturalnych.
'''


from zad2testy import runtests

def prepTabCopy(tab, i):
    newVal = tab[i]+tab[i+1]
    tabCP = tab[:]  #kopiowanie tablicy, aby nie naruszyć jej struktury (O(n))

    tabCP[i] = newVal   #wstawienie nowej wartości
    del tabCP[i+1]      #usunięcie elementu

    return tabCP


def opt_sum(tab):
    if len(tab) == 1:       #przypadek bazowy - sprawdzamy wynik końcowy
        return tab[0]

    # lowestAbsolute - największy wynik tymczasowy; ansInd - indeks pierwszego z dwóch elementów, który ten wynik tworzy.
    # Na poczatek zakładamy, że to pierwsza para elementów jest tą, którą szukamy

    lowestAbsolute = abs(tab[0] + tab[1])
    ansInd = 0

    #przeszukiwanie tablicy w poszukiwaniu najmniejszej wartości bezwzględnej
    for i in range(1, len(tab) - 1):
        tmp = abs(tab[i]+tab[i+1])
        if tmp < lowestAbsolute:
            lowestAbsolute = tmp
            ansInd = i

    # przygotowanie tablicy po dodaniu dwóch elementów o najmniejszej wartości bezwzględnej po zsumowaniu
    prepTab = prepTabCopy(tab, ansInd)

    # sprawdzamy rekurencyjnie, czy pozostałe dodawania nie mają większej wartości tymczasowej
    # max(a1,a2,a3...) = max(a1, max(a2, max(a3,...)))
    return max(lowestAbsolute, opt_sum(prepTab))



runtests( opt_sum )
