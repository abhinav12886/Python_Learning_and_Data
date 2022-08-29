def binary_search_rec(array, left, right, search_elem):
    if right >= left:
        mid_ind = (left + (right-1)) // 2

        if array[mid_ind] == search_elem:
            return "Found"
        elif search_elem < array[mid_ind]:
            binary_search_rec(array, left, mid_ind - 1, search_elem)
        else:
            binary_search_rec(array, mid_ind + 1, right, search_elem)

    else:
        return "Not Found"


if __name__ == "__main__":
    n = int(input("enter the length of list:- \n"))
    list = [int(input("Enter the list element:-\n")) for i in range(n)]
    target = int(input("enter the element to search for:-"))
    print(binary_search_rec(list, 0, n, target))
