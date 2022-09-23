def foo(n):
    print(n)
    if n == 1:
        return
    for i in range(n):
        foo(n - 1)


foo(4)

# time complexity O(n!)
