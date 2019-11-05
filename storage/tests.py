import time

from django.test import TestCase

# Create your tests here.
import random


def timer(func):
    def wrapper(*args, **kwargs):
        init_time = time.time()
        r = func(args[0])
        print(time.time() - init_time)
        return r

    return wrapper


@timer
def bubble_sort(lst):
    for i in range(0, len(lst)):
        for k in range(0, len(lst) - i - 1):
            if lst[k] > lst[k + 1]:
                lst[k], lst[k + 1] = lst[k + 1], lst[k]
    return lst


@timer
def some_sort(lst):
    for i in range(0, len(lst)):
        maximum = None
        for k in range(0, len(lst) - i):
            if maximum is None or lst[k] > maximum:
                maximum = lst[k]
        lst[len(lst) - i - 1] = maximum
    return lst


@timer
def some_sort_b(lst):
    for i in range(0, len(lst) // 2):
        maximum = None
        minimum = None
        for k in range(i, len(lst) - i):
            if maximum is None or lst[k] > maximum:
                maximum = lst[k]
            if minimum is None or lst[k] < minimum:
                minimum = lst[k]
        lst[len(lst) - i - 1] = maximum
        lst[i] = minimum
    return lst


if __name__ == '__main__':
    # liist = [6, 3, 5, 9, 1, 0, 4, 2, 7, 8, -1]
    liist = random.sample(range(-1000000, 1000000), 400000)
    bubble_sort(liist)
    some_sort(liist)
    some_sort_b(liist)
