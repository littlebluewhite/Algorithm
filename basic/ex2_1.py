# ex2_1.py
from array import *
x = array('f', [1.0, 2.0, 5.0, 6.5, 7.0])     
for data in x:
    print(data)


def resolve(n):
    result = array("f", n)
    for i in result:
        print(i)


if __name__ == "__main__":
    x = [1.0, 2.0, 5.0, 6.5, 7.0]
    resolve(x)

