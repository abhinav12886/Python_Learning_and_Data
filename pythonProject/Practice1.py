# design a calculator which will correctly solve all the problems except the following ones: -
# 45*3=555, 56+9=66, 56/6=44
# your program should take operator and the two values as input from the user and print the result

print("enter the first element:- ")
frst_val = int(input())
print("enter the second element:- ")
scnd_val = int(input())
print("enter the operator:- ")
op_val = input()

if (frst_val == 45 and scnd_val == 3) or (frst_val == 3 and scnd_val == 45) and op_val == "*":
    print("555")
elif (frst_val == 56 and scnd_val == 9) or (frst_val == 9 and scnd_val == 56) and op_val == "+":
    print("66")
elif (frst_val == 56 and scnd_val == 6) or (frst_val == 6 and scnd_val == 56) and op_val == "/":
    print("44")
elif op_val == "*":
    print("result = ", frst_val * scnd_val)
elif op_val == "+":
    print("result = ", frst_val + scnd_val)
else:
    print("result = ", frst_val / scnd_val)

