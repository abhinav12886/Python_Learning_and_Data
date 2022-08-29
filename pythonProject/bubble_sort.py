def bubble_sort(arr):
    for elem in range(len(arr) - 1):
        for index in range(len(arr) - 1 - elem):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]

    return arr


print(bubble_sort([45, 36, 78, 12, 45, 67]))
print(bubble_sort([]))
print(bubble_sort([67]))
print(bubble_sort([45, 45, 67]))
print(bubble_sort([45, 30, 20, 10, 5, 4, 3, 2, 1]))
