# # *args and **kwargs keywords..
#
# # We create a simple print function..
# def func(normal, *args, **kwargs):
#     print(normal)
#     for i in args:
#         print(i)
#     for key, value in kw.items():
#         print(f"Salary of {key} is {value}.")
#
#
# list = ["Harry", "Rajat", "Abhinav", "Vanshika"]
# normal1 = "im a good person"
# kw = {"harry": 30000, "rohan": 45000, "ravi": 36000}
#
# func(normal1, *list, **kw)

dict1 = {"key1": 1, "key2": 2}
dict2 = {"key2": 2, "key1": 1}
print(dict1 == dict2)