# 5. Find all of the words in a string that are less than 5 letters
str = input("Enter the string containing 2 or more words:- \n")
str = str.split(" ")
words = [i for i in str if len(i) < 5]
print(words)