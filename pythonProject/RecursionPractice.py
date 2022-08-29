# Q1:- Write a program of factorial using recursive approach.
#
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# n1 = int(input("Enter the number you want the factorial of:- "))
# print(factorial(n1))

# Q2:- Write a program to calculate the nth number of fibonacci series using recursion...
# 0 1 1 2 3 5 8 13 .....fibonacci series

# def fibonacci_nth(n):
#     """This function returns nth number of fibonacci sequence..."""
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci_nth(n - 1) + fibonacci_nth(n - 2)
#
#
# number = int(input("enter the number:- "))
# print(fibonacci_nth(number))


# Q3. Write a program to find the sum of a list of numbers.

# n = int(input("Enter the number of elements you want to add:- "))
# list2 = []
#
#
# def sum_rec(list1):
#     """This functions will give sum of numbers in a list"""
#     if len(list1) == 1:
#         return list1[0]
#     else:
#         return list1[0] + sum_rec(list1[1:])
#
#
# while n > 0:
#     l = int(input("Enter the element you want to add:- "))
#     list2.append(l)
#     n -= 1
#
# print("Sum of numbers is:- ", sum_rec(list2))


