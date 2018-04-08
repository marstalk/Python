import pdb


def test_var_args(f_arg, **kwargs):
    print(f_arg)

    for key, value in kwargs.items():
        print("{0}:{1}".format(key, value))


test_var_args("welcome", name="mars", age=10)

#print(type((1, 2, 3)))
#print(type([1, 2, 3]))
#print(type({"name": "mars", "age": 12}))

args = {"name": "mars", "age": 12}
test_var_args("welcome", **args)

test_var_args("peter")
