def Selection_sort(arr):
    for i in range(len(arr)):  # looping the array to check for all element
        min_index = i  # selecting the min element in this case (first index element).
        for j in range(i + 1, len(arr)):  # looping from one index ahead elem from the min elem to the len(arr)
            if arr[min_index] > arr[j]:  # checking if min index element is greater than the one ahead or not
                min_index = j  # if true then make min_index to be equal to j.

        arr[i], arr[min_index] = arr[min_index], arr[i]  # swaping the element

    return arr


print(Selection_sort([34, 2, 56, 28, 64]))

# Algo:---------
# Initialize minimum value(min_idx) to location 0
# Traverse the array to find the minimum element in the array
# While traversing if any element smaller than min_idx is found then swap both the values.
# Then, increment min_idx to point to next element
# Repeat until array is sorted

# Selection sort is a simple sorting algorithm. This sorting algorithm is an in-place comparison-based algorithm in
# which the list is divided into two parts, the sorted part at the left end and the unsorted part at the right end.
# Initially, the sorted part is empty and the unsorted part is the entire list.
