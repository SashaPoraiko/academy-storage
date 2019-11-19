import re
import time
import random


def timer(func):
    def wrapper():
        init_time = time.time()
        func()
        print(time.time() - init_time)

    return wrapper()


#
# @timer
# def test():
#     print('lol')


# print(type(test()))
#
# lst = [arr for arr in range(10)]
# print(type(lst), lst)
# gen_set = {arr for arr in range(3, 8) if arr % 2}
# print(type(gen_set), gen_set)
# gen_exp = (arr for arr in range(9, 150))
# print(type(gen_exp), gen_exp)
#
# r_list = [random.randrange(10) for _ in range(10)]
# print(r_list)
#
# the_dict = {1: True, 2: False, 3: 13, 4: 18, 5: 'string'}
# the_list = [[the_dict[i]] for i in the_dict]
#
# a = {1: 10, 2: 20, 3: 30}
# b = [[i, a[i]] for i in a]
#
# print(the_list)

lst_1 = [random.randrange(200) for i in range(150)]








