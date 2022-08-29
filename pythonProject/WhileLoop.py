# 1.
# Write a program which will keep on taking input from user until a number greater
# than 100 is entered.
"""
while (True):
    user_inp = int(input("Enter the number:- "))
    if user_inp <= 100:
        continue
    else:
        break
"""
# 2.
# write a program of guessing the number , first user will enter the number and the second
# user will guess the number if the user enter number less than the actual it should
# display less than the required num ,or if the num is greater then the req than it should display
# entered number is greater than the required, at correct guess it should print won ,9 chances to guess
# and if lose print game over.
"""
i = 10
user_inp = int(input("first player enter the number:- "))
while i > 0:
    i = i - 1
    print("Now chances left:- ", i)
    user_inp1 = int(input("second player enter the number:- "))
    if user_inp1 < user_inp:
        print("entered num is less than the required num, please try again ")
    elif user_inp1 > user_inp:
        print("entered num is greater than the required ")
        continue
    else:
        print("You guessed correct , YOU WON!! ")
        break
"""
