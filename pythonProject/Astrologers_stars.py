# Write a program which takes in input the number of rows(n) to print the star pattern and
# take the boolean value as 1 and 0 and type cast it to true or false ,
# when the its 1(true) pattern should be in downward inc stars else when it is 0(false) it must be in
# downward dec star pattern..

n = int(input("Enter the number of rows:-  "))
bool = int(input("Enter the boolean value \"1\" for True and \"0\" for False :-  "))

if bool == 1:
    for i in range(0, n+1):
        for j in range(i):
            print("*", end="")
        print("")
else:
    for i in range(n, 0, -1):
        for j in range(0, i):
            print("*", end="")
        print("\r")



