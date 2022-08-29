# q1. write a generator function to print fibonacci series.
# def fibonacci(n):
#     """
#     this function will print fibonacci series..
#     """
#     a, b = 1, 1
#     while b < n:
#         a, b = b, a + b
#         yield a
#
#
# for i in fibonacci(int(input("Enter the range upto which you want to print the series:- "))):
#     print(i)
#
#
# q2. write a generator function  to print factorial of a number.
# def factorial(n):
#     c = 1
#     for i in range(1, n + 1):
#         c = c * i
#
#     yield c
#
#
# x = factorial(int(input("Enter the number whose factorial you want:- ")))
# print(x.__next__())
#
# q3. write a generator function to iterate over a given string.
# def stringgen(string):
#     for i in range(len(string)):
#         yield string[i]
#
#
# for i in stringgen(input("Enter the string :- ")):
#     print(i)
#
# int is not iterable ...
