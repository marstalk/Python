import math


def get_prime(start_num):
    num = start_num
    while num < 99999999999:
        num += 1
        if is_prime(num):
            yield num


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


for i in get_prime(900):
    print(i)

