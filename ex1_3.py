# ex1_3.py
import itertools
import time

x = ['a', 'b', 'c', 'd', 'e', 'f']
perm = itertools.permutations(x)
n = 0
for i in perm:
    n += 1
    print(i)
print("總共有 %d 組合方式" % n)



def resolve(x):
    perm = itertools.permutations(x)
    for i in perm:
        print(i)


if __name__ == "__main__":
    before_t = time.time()
    resolve(x)
    after_t = time.time()
    print(after_t-before_t)














