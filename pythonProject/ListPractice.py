# LIST PRACTICE...

# 1:- WRITE A PROGRAM TO SWAP THE FIRST AND THE LAST ELEMENT OF A LIST.
"""
list1 = ["sheetal", "abhinav", "rahul", "vivek", 1, 2, 3]
print(list1)
x = list1[0]
list1[0] = list1[-1]
list1[-1] = x
print(list1)
"""
# 2:- write a program to swap the elements when there position(index) is given...
from typing import List

list1 = [1, 2, 3, 4, 5, 6, 7]
print(list1)
print("length of the list is: ", len(list1))
x = int(input("Enter the position of the first element you want to swap under the length: "))
y = int(input("Enter the position of the second element you want to swap under the length: "))
list1[x-1], list1[y-1] = list1[y-1], list1[x-1]
print(list1)