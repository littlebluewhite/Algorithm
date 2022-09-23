def foo(array: list):
    s = ""
    for i in array:
        s += i
    print(s)
    print("--------")

    if len(array) <= 1:
        return

    mid_index = len(array) // 2
    foo(array[0: mid_index])
    foo(array[mid_index:])


foo(["a", "b", "c", "d", "e", "f", "g", "h"])

# time complexity O(n*log(n))
