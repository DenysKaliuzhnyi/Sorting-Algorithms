import sorted
import functools
import time
import random
random.seed(1)


def avrgtime(func=None, *, n_iter=100, comments=""):
    if func is None:
        return lambda func: avrgtime(func, n_iter=n_iter)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        if comments:
            print(comments.ljust(10, " "), end="")
        print(func.__name__, end=" ... ")
        sum = 0
        result = None
        for i in range(n_iter):
            tick = time.perf_counter()
            result = func(*args, **kwargs)
            sum += time.perf_counter()-tick
        print(sum / n_iter)
        return result

    return inner


algs = [sorted.bubble, sorted.insert, sorted.choice, sorted.heap, sorted.merge, sorted.quick]
n_nums = 5000
n_iter = 10
arr1 = [random.randint(0, 1000) for _ in range(n_nums)]
arr2 = [i for i in range(n_nums)]
arr3 = [i for i in range(n_nums-1, -1, -1)]
arr4 = [random.choice([0, 1]) for _ in range(n_nums)]

for alg in algs:
    avrgtime(alg, n_iter=n_iter, comments="random")(arr1)
    avrgtime(alg, n_iter=n_iter, comments="sorted")(arr2)
    avrgtime(alg, n_iter=n_iter, comments="reversed")(arr3)
    avrgtime(alg, n_iter=n_iter, comments="bool")(arr4)
    print()


