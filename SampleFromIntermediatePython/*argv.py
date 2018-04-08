def test_var_argv(f_arg, *args):
    print("first normal arg:" + f_arg)

    for arg in args:
        print("another arg is: " + arg)


##test_var_argv("hello", "mars", "welcome" , "to", "intermediatePython")

args = ("mars", "peter", "tim")
test_var_argv("welcome", *args)

