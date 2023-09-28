# implementation of quicksort algorithm choosing pivot as median of three
def quickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)


def partition(arr, low, high):
    pivot = medianOfThree(arr, low, high)

    i = low-1
    for j in range(low, high):

        # swap elements smaller than pivot with ++i
        if arr[j] <= arr[pivot]:
            i = i+1
            (arr[i], arr[j]) = (arr[j], arr[i])
    
    (arr[i+1], arr[high]) = (arr[high], arr[i+1]) # final pivot swap
    return i+1 # return position where partition is done

    
def medianOfThree(arr, low, high):
    mid = (low+high)//2

    biggest = bigger(arr, low, bigger(arr, mid, high))

    if biggest == low:
        return bigger(arr, mid, high)
    elif biggest == high:
        return bigger(arr, low, mid)
    else:
        return bigger(arr, low, high)


def bigger(arr, a, b):
    if arr[a] > arr[b]:
        return a
    else:
        return b

        
if __name__ == "__main__":
    arr = [10, 3, 8, 9, 11]
    quickSort(arr, 0, len(arr)-1)
    print(arr)
        