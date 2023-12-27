import functools
@functools.lru_cache(maxsize=2)
def square(num):
    print("running", num)
    return num ** 2