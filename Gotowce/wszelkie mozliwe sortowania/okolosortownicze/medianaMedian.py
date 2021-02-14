def srodkowyInd(arr):
    if len(arr)%2 == 0:
        return len(arr)//2 - 1
    else:
        return len(arr)//2
        
def medianaMedian(arr):
    n = len(arr)
    if n <= 5:
        arr.sort()
        m = srodkowyInd(arr)
        return arr[m]
    else:
        tablicaMedian = []
        for i in range(0, n, 5):
            pom = arr[i:(i+5)]
            pom.sort()
            m = srodkowyInd(pom)
            tablicaMedian.append(pom[m])
    return medianaMedian(tablicaMedian)


array = [ 3, 4, 5, 2, 1, 7, 8, 12, 11, 9, 13, 12, 24, 982, 45, 233, 23, 13,11, 35, 26]
x = medianaMedian(array)
print(x)
