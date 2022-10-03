def foo(n):
    if n <= 1:
        print("hooray")
        return
    print(n)
    foo(n/2)


foo(50)

# time complexity O(log(n))
