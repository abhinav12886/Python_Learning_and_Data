def Insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        last = i - 1
        while last >= 0 and key < arr[last]:
            arr[last + 1] = arr[last]
            last = last - 1
        arr[last + 1] = key
    return arr

arr = [34, 36, 12, 6, 7]
print(Insertion_sort(arr))
