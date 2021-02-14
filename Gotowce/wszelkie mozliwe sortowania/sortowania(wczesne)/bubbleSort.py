def bubbleSort(a):
    n = len(a)
    sortedList = False
    while not sortedList:
        for i in range(n-1, -1, -1):
            sortedList = True
            for j in range(i, n-1):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
                    sortedList = False

if __name__ == "__main__":
    a = [3, 2, 5, 4, 1]
    bubbleSort(a)
    print(a)
