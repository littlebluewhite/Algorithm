# ex1_1.py
import time


def factorial(n):
    """ 計算n的階乘, n 必須是正整數 """
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))


def resolve(n):
    if n > 1:
        return n*resolve(n-1)
    else:
        return 1


if __name__ == "__main__":
    n = 20
    before_t = time.time()
    factorial(100)
    after_t = time.time()
    print(after_t-before_t)
    print("排列組合有 %d 個方法" % factorial(n))

    before_t = time.time()
    resolve(100)
    after_t = time.time()
    print(after_t-before_t)
    print("排列組合有 %d 個方法" % resolve(n))
