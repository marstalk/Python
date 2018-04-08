
def hi(name="mars"):
    print("now you are in the hi function")

    def greet(name):
        return "now you are in the function of greet:" + name

    def welcome(name):
        return "welcome to welcomeFunction, " + name

    print(greet(name))
    print(welcome(name))

    print("now you are back to hi function")

hi("peter")