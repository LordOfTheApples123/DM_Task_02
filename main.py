
import functools
import math

from sympy import *

def comparator(f0, f1):
    limitExpr = limit(f1 / f0, x, oo)
    print(limitExpr)
    if limitExpr > 0:
        return -1
    if limitExpr < 0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    x = Symbol('x')
    f0 = sqrt(2) ** (log(x, 2))
    f1 = x ** 2
    f2 = factorial(x)
    f3 = factorial(log(x, 2))
    f4 = (3 / 2) ** x
    f5 = x ** 3
    f6 = log(x, 2) ** 2
    f7 = log(factorial(x), 2)
    f8 = 2 ** (2 ** x)
    f9 = x ** (1 / log(x, 2))
    f10 = log(log(x))
    f11 = x * 2 ** x
    f12 = x ** (log(log(x), 2))
    f13 = log(x)
    f14 = 1
    f15 = 2 ** (log(x, 2))
    f16 = log(x, 2) ** log(x, 2)
    f17 = math.e ** x
    f18 = 2 * factorial(x)
    f19 = sqrt(log(x, 2))
    f20 = 2 ** (2 * sqrt(log(x, 2)))
    f21 = x * log(x, 2)
    f22 = 2 ** x
    f23 = x
    f = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23]
    print(sorted(f, key=functools.cmp_to_key(comparator)))