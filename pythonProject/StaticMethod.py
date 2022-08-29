# These methods work as a independent function which doesnt take any class name(self or cls)
# or any instance name as argument.

class Vehicle:
    pass

    @staticmethod
    def printgood(string):
        print("this is ", string)


harry = Vehicle()
harry.printgood("harry")
