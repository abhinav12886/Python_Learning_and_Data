# # to open a file
#
# f = open("abhi.txt", "a")
# # print(content)
#
# # for x in f:
# #     print(x, end="")
#
# # content = f.readlines()
# # print(content)
#
# f.write("abhinav is a good\n")
#
# f.close()

# To perform close and open operation all in once ..
# use "with" block as stated down

with open("abhi.txt") as f:
    a = f.read()
    print(a)
