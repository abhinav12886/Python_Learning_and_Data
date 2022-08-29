# super() and method overrriding

class A:
    classvar1 = "im a class variable of class A"

    def __init__(self):
        self.var1 = "im an instance var1 of class A"
        self.var2 = "im an instance var2 of class A"
        self.special = "Special"


class B(A):
    classvar1 = "Im an class var of class B "

    def __init__(self):
        # if we use super() func in here it will print var1 of B class , but in place 2 it will print
        # var1 of class A, because we are calling it in last rather than at first ...

        self.classvar1 = "Im an instance var1 of class B "
        # self.classvar2 = "Im an instance var2 of class B "
        # self.special = "Special1"
        self.var1 = "im an instance var1 in class B"
        super().__init__()  # 2


a = A()
b = B()
print(b.special, b.var1)
