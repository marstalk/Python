#global return

# def add(a, b):
#     global result
#     result = a+b
#
#
# add(1,3)
#
# print(result)


def add(a, b):
    return a, b


a, b = add(12, 23)

print(a, b)
