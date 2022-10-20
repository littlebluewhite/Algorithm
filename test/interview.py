def fib(max):
    a = []
    a.insert(0, 0)
    a.insert(1, 1)
    print(a)
    for i in range(2, max + 1):
        a.insert(i, a[i - 1] + a[i - 2])
    return a[-1]


print(fib(100))
