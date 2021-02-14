from math import floor, ceil, log2

def findlevel(i):
    level = ceil(log2(i))
    c = 2**level - 1

    return c, level

class IntervalSums:
    def __init__(self, n):
        self.c, self.maxlevel = findlevel(n)
        self.aux = [0 for _ in range(self.c + n)]
        self.n = n

        # c to najmniejsza potęga dwójki większa od n zmniejszona o jeden,
            # czyli liczba wezłow na wyzszym poziomie niz bazowe n
        # level to wysokosc kopca węzłów (liczona od 1, z wyłączeniem wartości pojedynczych (w zasadzie log2(c+1)))
        # aux - kopiec/drzewo akumulujące wartości synów
        # n jest w sumie niepotrzebny, ale możliwe, że da się nim przyśpieszyć algorytm dla danych nie będących potęgą dwójki, ale jeszcze tego nie wykminiłem

    def buildheap(self, i):
        if i >= 0:
            parent = (i-1)//2
            left = 2*i + 1
            right = 2*i + 2
            n = len(self.aux)

            self.aux[i] = 0
            self.aux[i] += self.aux[left]
            if right < n:
                self.aux[i] += self.aux[right]
            self.buildheap(parent)

    def set(self, i, val):  #dodawanie wartości do kopca
        c = self.c
        self.aux[c+i] = val
        parent = (c+i-1)//2     #c+i to rzeczywisty indeks elementu w self.aux
        self.buildheap(parent)

    def findinterval(self, ind):       #znajdowanie przedziału przypisanego węzłowi (to jest trochę czarna magia, jak chcesz, to Ci to rozrysuję)
        if ind > self.c:
            result = (ind - self.c, ind - self.c)
            return result

        ind += 1
        lvl = self.maxlevel - floor(log2(ind))
        jump = 2**lvl
        tmp = ind - 2**floor(log2(ind))

        a = jump*tmp
        b = a + jump-1
        return (a, b)


    def interval(self, i, j):
        def interval_aux(self, i, j, ind):
            a,b = self.findinterval(ind)
            mid = (a+b+1)//2

            if a == i and b == j:
                return self.aux[ind]
            else:
                left = 2*ind + 1
                right = 2*ind + 2
                if a <= i and j < mid:      #szukany przedział znajduje się w lewym synu
                    return interval_aux(self, i, j, left)
                elif mid <= i and j <= b:   #j.w. ale w prawym
                    return interval_aux(self, i , j, right)
                else:                       #szukany przedział jest "przecięty" przez środek przedziału obecnego wezła
                    result = interval_aux(self, i , mid-1, left)
                    result += interval_aux(self, mid, j, right)
                    return result

        return interval_aux(self, i, j, 0)

T = IntervalSums(5)
T.set(0, 18)
T.set(1, 2)
T.set(2, 3)
T.set(3, 10)
T.set(4, 6)
print(T.interval(0,4))
T.set(3, 2)
print(T.interval(0,4))




