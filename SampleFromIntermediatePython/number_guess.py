

guess = 0

correct_num = 17

while guess != correct_num:
    i = input("one more try:")
    print(type(i))
    guess = int(i)
    #guess = input("one more try:")
print("Congratulations, the answer is :" + str(guess))