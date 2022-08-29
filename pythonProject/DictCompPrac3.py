# First, create a range from 100 to 160 with steps of 10.
# Second, using dict comprehension, create a dictionary where each number in the range
# is the key and each item divided by 100 is the value.
dict = {i: i/100 for i in range(100, 160, 10)}
print(dict)