# Function caching allows us to cache the return values of a function depending on the
# arguments. It can save time when an I/O bound function is periodically called with
# the same arguments. Before Python 3.2 we had to write a custom implementation.

# -------------------------------------- lru_cache():- ------------------------------------------

# lru_cache() is one such function in functools module which helps in reducing the
# execution time of the function by using memorization technique.
#
# Syntax:
# @lru_cache(maxsize=128, typed=False)
#
# Parameters:
# maxsize:This parameter sets the size of the cache, the cache can store upto maxsize
# most recent function calls, if maxsize is set to None, the LRU feature will be disabled
# and the cache can grow without any limitations
# typed:
# If typed is set to True, function arguments of different types will be cached separately.
# For example, f(3) and f(3.0) will be treated as distinct calls with distinct results
# and they will be stored in two separate entries in the cache

from functools import lru_cache
import time


@lru_cache(maxsize=1, typed=False)
def func1(n):
    print(" im in func1")
    time.sleep(n)
    return n


if __name__ == "__main__":
    func1(2)
    print("func1 printed")
    func1(2)
    print("func1 printed")
    func1(5)
    print("func1 called ")
    func1(5)
    print("func1 printed end")
    func1(4)
    print("------")