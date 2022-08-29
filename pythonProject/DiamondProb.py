# confusion of , which class will use which class's method and var in multiple inheritance

class A:
    def nothing(self):
        print("im in class A")


class B(A):
    def nothing(self):
        print("im in class B")


class C(A):
    def nothing(self):
        print("im in class C")


class D(C, B):
    pass


b = D()
b.nothing()
