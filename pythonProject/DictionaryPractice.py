# 1.
# Create a dictionary and display its keys alphabetically.
# Display both the keys and values sorted in alphabetical order by the key.
# Same as part (ii), but sorted in alphabetical order by the value.
keys_value = {}
keys_value[1] = "rohan"
keys_value[4] = "vivek"
keys_value[3] = "roham"
keys_value[5] = "rohit"
keys_value[2] = "abhinav"
print("keys:- ")
for i in sorted(keys_value.keys()):
    print(i, end=" ")

print("\nkey value-pairs:- ")
for i in sorted(keys_value):
    print((i, keys_value[i]), end=" ")

print("\nsorted by value:- ")
for i in sorted(keys_value.values()):
    print(i, end=" ")