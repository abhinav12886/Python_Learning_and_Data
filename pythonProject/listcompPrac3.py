# 4. Remove all of the vowels in a string
list1 = ["a", "e", "i", "o", "u"]
str1 = input("Enter the string:- \n")
no_vowel = "".join([char for char in str1 if char not in list1])
print(no_vowel)
