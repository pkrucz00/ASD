def partition(a, start, stop):
    i = start
    for j in range(start, stop):
        if a[stop] > a[j]:
            a[i],a[j]=a[j],a[i]
            i += 1
    a[stop],a[i] = a[i], a[stop]
    return i

def quickSort(a, start, stop):
    if start < stop:
        pivot = partition(a, start, stop)
        quickSort(a, start, pivot - 1)
        quickSort(a, pivot + 1, stop)

if __name__ == "__main__":
    a = [3, 2, 5, 4, 1, 8 , 6 , 7 , 9]
    quickSort(a, 0, len(a) - 1)
    print(a)
