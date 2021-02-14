def selectSort(a):
    n = len(a)
    for i in range(n-1):
        indMin = i
        for j in range(i+1, n):
            if a[indMin] > a[j]:
                indMin = j
        a[indMin], a[i] = a[i], a[indMin]

if __name__ == "__main__":
    a = [3, 2, 5, 4, 1]
    selectSort(a)
    print(a)
