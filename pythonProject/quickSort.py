def partition(arr, start, end):
    pivot_elem = arr[start]

    while start < end:
        while arr[start] < pivot_elem:
            start += 1

        while arr[end] > pivot_elem:
            end -= 1

        arr[start], arr[end] = arr[end], arr[start]

    arr[start], arr[end] = arr[end], arr[start]

    return end


def quickSort(arr, start, end):
    if start < end:
        p = partition(arr, start, end)
        quickSort(arr, start, p - 1)
        quickSort(arr, p + 1, end)


test_cases = [
    [12, 11, 13, 5, 6, 7],
    [],
    [3],
    [9, 8, 7, 2],
    [1, 2, 3, 4, 5],
]
for i in range(len(test_cases)):
    start = 0
    end = len(test_cases[i]) - 1
    quickSort(test_cases[i], start, end)
    print(test_cases[i])

# Worst Case: O(n^2)
# The worst case occurs when the partition process always picks greatest or smallest element as pivot.
# T(n) = T(n-1) + \theta(n)

# Best Case: O(nLogn)
#  The best case occurs when the partition process always picks the middle element as pivot.
#  Following is recurrence for best case.
#  T(n) = 2T(n/2) + \theta(n)

