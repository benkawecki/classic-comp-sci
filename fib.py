import timeit
from functools import lru_cache
memo = {0: 0, 1:1}


def fib1(n):
    """regular recursion solution"""
    if n < 2:
        return n
    else:
        return fib1(n-1) + fib1(n-2)

def fib2(n):
    """memoization"""
    if n not in memo:
        memo[n] = fib2(n-1) + fib2(n-2)
    return memo[n]

@lru_cache(maxsize=0)
def fib3(n):
    """std lib memoization"""
    if n < 2:
        return n
    else:
        return fib3(n-1) + fib3(n-2)  

def fib4(n):
    """iteration"""
    if n == 0: return n
    first, second = 0,1
    for i in range(1,n):
        first, second = second, first + second
    return second

def fib5(n):
    pass


if __name__ == "__main__":
    fib_nums = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,]
    for fib_func in [fib1, fib2, fib3, fib4]:
        for i, num in enumerate(fib_nums):
            assert fib_func(i) == num 
        t = timeit.timeit(
            f'{fib_func.__name__}(20)', 
            setup=f'from __main__ import {fib_func.__name__}', 
            number=10
        )
        print(f"The time for {fib_func.__name__} was {t}")
    