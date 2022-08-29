from abc import ABC, abstractmethod


class shape(ABC):

    @abstractmethod
    def print_area(self):
        pass
        # self.length = 20
        # self.breadth = 20


class rectangle(shape):
    def __init__(self):
        print("enter the length of rectangle")
        self.length = float(input())
        print("enter the breadth of rectangle")
        self.breadth = float(input())

    def print_area(self):
        return self.length * self.breadth


b = rectangle()
print(b.print_area())