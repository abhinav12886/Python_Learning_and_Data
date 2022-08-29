# 2. dictionary Comprehension

# Syntax:- output_dict = {key:value for (key, value) in iterable if (key, value satisfy this condition)}

# Example #1: Suppose we want to create an output dictionary which contains only the odd numbers
# that are present in the input list as keys and their cubes as values.

# input_list = [1,2,3,4,5,6,7]
#
# dict_using_comp = {var:var ** 3 for var in input_list if var % 2 != 0}
#
# print("Output Dictionary using dictionary comprehensions:", dict_using_comp)
