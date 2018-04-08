

def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for i in fibon(10):
    print(i)

num = fibon(10)
print(num)


my_str = "welcome";
for i in iter(my_str):
    print(i)


