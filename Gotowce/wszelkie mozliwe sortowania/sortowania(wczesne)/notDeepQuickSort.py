def partition(a, start, stop):
    n = stop - start
    i = start
    for j in range(start, stop):
        if a[stop] > a[j]:
            a[i],a[j]=a[j],a[i]
            i += 1
    a[stop],a[i] = a[i], a[stop]
    return i

def quickSort(A, i, j):
    if i < j:
        pivot = partition(a, i, j)
        while i < j:
            if pivot < (i + j)/2        #jeśli pivot wyladowal na lewo od srodkowego elementu
                quickSort(a, pivot + 1, j)   #najpierw wiekszy fragment
                quickSort(a, i, pivot - 1)
        else:   #jesli jest dokladnie na srodku lub po prawej od srodkowego elementu
            quickSort(a, i, pivot - 1)  #najpierw wiekszy fragment
            quickSort(a, pivot + 1, j)
