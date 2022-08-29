class Employee:
    def __init__(self, aname, aage):
        self.name = aname
        self.age = aage

    @classmethod
    def from_str(cls, string):
        # params = string.split("-")
        # return cls(params[0], params[1])
        # to use one liner we use *args statement
        return cls(*string.split("-"))


harry = Employee("abhinav", 21)
print(harry.name, harry.age)

harry = Employee.from_str("abhishek-23")
print(harry.name, harry.age)
