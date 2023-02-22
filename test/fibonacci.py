# def fib(n: int) -> int:
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# ans = fib(6)
# print(ans)


def fib(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    n1 = 0
    n2 = 1
    i = 2
    res = 0
    while i <= n:
        res = n1 + n2
        n1, n2 = n2, res
        i += 1
    return res


print(fib(100))
