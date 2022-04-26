# ex12_3.py   
def fun(n):
    if n == 1:
        return 1
    else:
        return fun(n - 1) + 1.0 / n

n = eval(input('請輸入整數 : '))
for i in range(1, n + 1):
    print('f({}) = {}'.format(i, fun(i)))           












































def my_function(n):
    if n == 1:
        print(f"f(1) = 1")
        return 1
    result = my_function(n-1) + 1/n
    print(f"f({n}) = {result}")
    return result

n = int(input("請輸入整數 : "))
my_function(n)
