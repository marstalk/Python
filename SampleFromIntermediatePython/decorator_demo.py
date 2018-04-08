

def hi(name="mars"):
    return "hi " + name

print(hi())

greet = hi
print(greet())

del hi

##print(hi())
print(greet())