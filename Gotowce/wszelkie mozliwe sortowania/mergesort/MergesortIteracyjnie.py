L=[1,3,8,34,55,21,13,5,2]
print(L)
import math
def merge (L, start, center, finish):
    i = start
    j = center + 1
    L2 = []
    while (i <= center) and (j <= finish):
        if L[j] < L[i]:
            L2.append(L[j])
            j +=1
        else:
            L2.append(L[i])
            i += 1

    if i <= center:
        while i <= center:
            L2.append(L[i])
            i +=1

    else:
        while j <= finish:
            L2.append(L[j])
            j +=1

    s = finish - start + 1
    i = 0
    while i < s:
        L[start + i] = L2[i]
        i += 1
    return L


def merge_sort (L):
    n=len(L)
    i=1
    while i < n:
        j=0
        while j < n:
            if (i+j-1) < n and (j+2*i-1)< n :
                merge(L , j , i+j-1, j+2*i-1)
            j+=1
        i*=2

merge_sort(L)
print(L)
