import functools


@functools.lru_cache
def fib(n: int) -> int:
    if n in [0, 1]:
        return 1

    return fib(n - 1) + fib(n - 2)
