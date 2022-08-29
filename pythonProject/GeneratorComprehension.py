# 4. generator comprehensions

# Syntax:- Generator Comprehensions are very similar to list comprehensions. One difference between them is that

# generator comprehensions use circular brackets whereas list comprehensions use square brackets.
# output_gen = (output_exp for var in input_list if (var satisfies this condition))

# input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
#
# output_gen = (var for var in input_list if var % 2 == 0)
#
# print("Output values using generator comprehensions:", end = ' ')
#
# for var in output_gen:print(var, end = ' ')