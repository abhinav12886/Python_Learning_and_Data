y = "rambabuasharmabaefv"
"""""
print(y[:5], end="")
print(y[6:11], end="")
print(y[12:])

print(y[:5], y[6:11], y[12:])
print(y.center(20, "0"))
"""

# list is mutable but tuple is immutable
# list1 = [] : syntax of list
# tuple1 = () : syntax of tuple.
# dictionary = {"key":"value"} : syntax for dictionary(mutable)
# s = set() : syntax for set(immutable)
# LDM:-  List Dictionary Mutable
"""
question = Create a dictionary and take input from the user and return the meaning of that word from the dictionary.

dict1 = {"mutable": "can be changed",
         "immutable": "cant be changed",
         "long": "lengthy",
         "important": "high priority"}
print(dict1.keys())
user_inp = input("enter the word you want the meaning of from the above list:  ")
user_inp = user_inp.lower()
if user_inp == "mutable":
    print(dict1.get("mutable"))
elif user_inp == "immutable":
    print(dict1.get("immutable"))
elif user_inp == "long":
    print(dict1.get("long"))
else:
    print(dict1.get("important"))
"""

















