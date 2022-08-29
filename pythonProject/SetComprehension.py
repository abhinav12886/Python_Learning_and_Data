# 3. Set Comprehensions:----

# Syntax:- Set comprehensions are pretty similar to list comprehensions.

# The only difference between them is that set comprehensions use curly brackets { }.
# output_set = {output_exp for var in input_list if (var satisfies this condition)}

# Example #1 : Suppose we want to create an output set which contains only the even numbers
# that are present in the input list. Note that set will discard all the duplicate values.

# input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
#
# set_using_comp = {var for var in input_list if var % 2 == 0}
#
# print("Output Set using set comprehensions:",
#                               set_using_comp)