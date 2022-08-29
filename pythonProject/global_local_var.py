l = 10  # global variable


def func1():
    m = 20  # local variable
    #   print(l) --> it will work as it is inside the scope of global variable.
    print(m)


func1()
# print(m) --> this will give error as it is outside the scope of local variable m
