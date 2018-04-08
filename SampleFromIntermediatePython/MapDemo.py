#map能够将一个函数映射到一个列表上，这个列表可以是任何类型，也包括方法！！！

#将一个列表的所有值+2

my_list = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 0]
new_list = list(map(lambda x: x+2, my_list))


print(new_list)

for i in map(lambda x: x+2, my_list):
    print(i)



