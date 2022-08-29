# json file does not have comments and always use double quotes in json file
import json

# json.loads()
data = '{"var1":"harry","var2":"abhi"}'
data1 = {"var1": "harry", "var2": "abhi"}
# print(data, " 1 \n")
#
# print(data["var1"])  # this will give an error because it is a string not like a dictionary object
#
# r = json.loads(data)  # loads takes in input json string and returns a python dictionary object
# print(r, "2 \n")
# print(r["var1"])

# ------------------------------------------------------------------------------------------------------

# The json.load() is used to read the JSON document from file and convert it into python dictionary
# and The json.loads() is used to convert the JSON String document into the Python dictionary.
# json.load()
with open("abhi.json", "w") as write_file:  # here we created a json file
    json.dump(data1, write_file)  # here we added data1 to the json file(abhi.json)

with open("abhi.json", "r") as read:  # here we read the json file
    print(json.load(read))  # here we print the file content using json.load method

# json.dumps():- If you have a Python object, you can convert it into a JSON string
# by using the json.dumps() method.

x = json.dumps(data1)
print(x)

# json.dumps() method can convert a Python object into a JSON string.
#
# Syntax: json.dumps(dict, indent)
#
# Parameters:
# dictionary – name of dictionary which should be converted to JSON object.
# indent – defines the number of units for indentation

# json.dump() method can be used for writing to JSON file.
#
# Syntax: json.dump(dict, file_pointer)
#
# Parameters:
#
# dictionary – name of dictionary which should be converted to JSON object.
# file pointer – pointer of the file opened in write or append mode.