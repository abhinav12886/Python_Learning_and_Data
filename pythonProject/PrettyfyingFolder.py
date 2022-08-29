# Problem Statement:--------------------------------------------
# The task you have to perform is "Oh Soldier Prettify my Folder."
#
# Suppose you have a folder, and its path is also given. You have to create a function
# which takes three input arguments, which are:
#
# def soldier("C://", "harry.txt", "jpg")
#
# 1.Full Path of the folder as input strings.
# 2.Dictionary file :- it will contain words separated by '\n' which i don't have to change
# 3.File Format

# The function will perform three tasks:-------------------------
# 1.First, it will check all the files present in the folder whose paths are given as an input argument.
# 2.Then it will capitalize the first letter of each file. If the name of the file is present
#   in a dictionary file then it will not capitalize the first letter. It will only capitalize
#   the first letter of the files, which are not present in the dictionary file.
# 3.The function renames the file names to number in range of 1 to100 whose format is the same as
#   mentioned in the input parameter like 1.jpg.

# After performing these tasks, your folder will prettify as all the first letters of the files
# in the folder will be capitalize except for those files whose names are present in the dictionary file.
# And the files having the same format as given in the input argument will rename to number in
# the range of 1-100.
import os


def soldier(path, file):
    os.chdir(path)
    with open(path) as f:
        for files in f:
            if files not in open(file, "rt"):
                files.capitalize()


soldier(r"C:\Users\$HINIGAMI\Desktop\filehandlingpractice", r"C:\Users\Abhi\PycharmProjects\pythonProject\filename1.txt")
# do it on own later--------debugging--------------------------