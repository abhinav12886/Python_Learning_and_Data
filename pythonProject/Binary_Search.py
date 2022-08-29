def binary_search(array, target, length_array):
    array.sort()
    left = 0
    right = length_array - 1
    while left <= right:
        middle_index = (left + right) // 2
        mid_elem = array[middle_index]
        # conditions
        if target == mid_elem:
            return "Found"
        elif target < mid_elem:
            right = middle_index - 1
        else:
            left = middle_index + 1
    return "Not Found"


if __name__ == "__main__":
    n = int(input("enter the length of list:- \n"))
    list = [int(input("Enter the list element:-\n")) for i in range(n)]
    target = int(input("enter the element to search for:-"))
    print(binary_search(list, target, n))
