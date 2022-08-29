# Create a dictionary from the list with same key:value pairs, such as: {"key": "key"}.
list = ["NY", "FL", "CA", "VT"]
dict = {i: i for i in list}
print(dict)