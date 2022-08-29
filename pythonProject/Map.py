# ----------MAP----------------------
# Q1. Write a Python program to triple all numbers of a given list of integers. Use Python map

# list1 = [1, 2, 3, 4, 5]

# def triple(num):
#     """This functions return triple of the number"""
#     return 3 * num


# print(list(map(triple, list1)))

# --------------------Now by using lambda expressions-------------------------------------

# print(list(map(lambda x: x * 3, list1)))

# q2. wap to add three list items using map and lambda------

# List1 = [1, 2, 3, 4, 5, 6]
# List2 = [1, 2, 3, 4, 5, 6]
# List3 = [1, 2, 3, 4, 5, 6]
#
# print(list(map(lambda x, y, z: x + y + z, List1, List2, List3)))

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Original list of integers:")
# print(nums)
# print("\nEven numbers from the said list:")
# even_nums = list(filter(lambda x: x%2 == 0, nums))
# print(even_nums)
# print("\nOdd numbers from the said list:")
# odd_nums = list(filter(lambda x: x%2 != 0, nums))
# print(odd_nums)

