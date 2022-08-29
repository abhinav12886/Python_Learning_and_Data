def mergeSort(my_array):
    if len(my_array) <= 1:
        return my_array

    middle = len(my_array) // 2
    left = my_array[:middle]
    right = my_array[middle:]

    left_result = mergeSort(left)
    right_result = mergeSort(right)

    return merge(left_result, right_result)


def merge(left_result, right_result):
    result = [None] * (len(left_result) + len(right_result))
    i = j = k = 0

    while i < len(left_result) and j < len(right_result):
        if left_result[i] <= right_result[j]:
            result[k] = left_result[i]
            i += 1
        else:
            result[k] = right_result[j]
            j += 1
        k += 1

    while i < len(left_result):
        result[k] = left_result[i]
        i += 1
        k += 1

    while j < len(right_result):
        result[k] = right_result[j]
        j += 1
        k += 1

    return result


if __name__ == "__main__":
    test_cases = [
        [12, 11, 13, 5, 6, 7],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5]
    ]
    for i in range(len(test_cases)):
        print(mergeSort(test_cases[i]))

# Time complexity of Merge Sort is  θ(nLogn) in all 3 cases (worst, average and best) as merge sort always divides
# the array into two halves and takes linear time to merge two halves.
# Auxiliary Space: O(n) Algorithmic Paradigm:
# Divide and Conquer
# Sorting In Place: No in a typical implementation
# Stable: Yes
# Merge Sort is useful for sorting linked lists in O(nLogn) time.
# However, merge sort is generally considered better when data is huge and stored in external storage.

# Why Quick Sort is preferred over MergeSort for sorting Arrays?
# Quick Sort in its general form is an in-place sort (i.e. it doesn’t require any extra storage),
# whereas merge sort requires O(N) extra storage, N denoting the array size which may be quite expensive.
