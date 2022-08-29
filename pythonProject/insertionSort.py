def insertionSort(a, n):
    for i in range(1, n):
        temp = a[i]

        j = i - 1
        while j >= 0 and a[j] > temp:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = temp


arr = [12, 11, 13, 5, 6]
insertionSort(arr, 5)
print(arr)

# Insertion Sort Algorithm :-----------
# To sort an array of size N in ascending order:

# Iterate from arr[1] to arr[N] over the array.
# Compare the current element (key) to its predecessor.
# If the key element is smaller than its predecessor, compare it to the elements before.
# Move the greater elements one position up to make space for the swapped element.

# This works by maintaining a sorted and unsorted array.
