class Employee:
    no_of_leaves = 34

    def __init__(self, cname, cage):
        self.name = cname
        self.age = cage

    @classmethod
    def change_no_of_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves


abhi = Employee("Abhinav", 23)
print(abhi.age, abhi.name)

# abhi.no_of_leaves = 32
# it is a new instance of the (no_of_leaves) variable, it didn't change
# the original class variable value
print(abhi.no_of_leaves)  # it will print that original value of the class variable

harry = Employee("harry", 24)
print(harry.no_of_leaves)
# it will print that original value of the class variable
# -----------------------------------------------------------------------------------------
# Now if we want to change the class variable value without
# using the class name variable

# we use the class method as defined above

abhi.change_no_of_leaves(21)
print(abhi.no_of_leaves)
