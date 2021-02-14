def partition(arr,low,high):
    i = ( low-1 )
    pivot = arr[high]

    for j in range(low , high):
        if   arr[j] < pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

def select(A, i):
    if len(A) == 1:
        return A[0]
    k = partition(A, 0, len(A) - 1)
    if i == k:
        return A[i]
    elif i < k:
        return select(A[:k-1], i)
    else:
        return select(A[k+1:], k-i)



A = [2,1,3,7]
print(select(A,2))