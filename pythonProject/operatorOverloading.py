# oprator overloading and dunder methods(__method__)...
# Methods which have double underscore(__) before and after the name of method then it is a dunder meth..

class A:
    no_of_leaves = 8

    def __init__(self, asalary):
        self.salary = asalary

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    # Addition dunder method
    def __add__(self, other):
        return self.salary + other.salary

    # Division dunder method
    def __truediv__(self, other):
        return self.salary / other.salary


class B(A):
    pass


emp1 = A(200)
emp2 = B(200)
print(emp1 + emp2)
print(emp1 / emp2)
