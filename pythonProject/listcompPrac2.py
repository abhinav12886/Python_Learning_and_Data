# 3. Count the number of spaces in a string
str = input("enter the string")
count = 0
number_of_spaces = len([space for space in str if space == " "])
print(number_of_spaces)