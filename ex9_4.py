# ex9_4.py
import random


def bubble_sort(nLst):
    length = len(nLst)
    for i in range(length-1):
        print("第 %d 次外圈排序" % (i+1))
        for j in range(length-1-i):
            if nLst[j] < nLst[j+1]:
                nLst[j],nLst[j+1] = nLst[j+1],nLst[j]
            print("第 %d 次內圈排序 : " % (j+1), nLst)
    return nLst

data = []
while True:
    val = input("請輸入數值(Q或q代表輸入結束) : ")
    if val == "Q" or val == "q":
        break
    data.append(int(val))
print("原始串列 : ", data)
print("排序結果 : ", bubble_sort(data))
















def quick_sort_dec(l1: list):
    if len(l1) <= 1:
        return l1

    right = []
    left = []
    piv = []
    target = random.choice(l1)
    for item in l1:
        if item == target:
            piv.append(item)
        elif item < target:
            left.append(item)
        elif item > target:
            right.append(item)
    return quick_sort_dec(right) + piv + quick_sort_dec(left)


data = []
while True:
    value = input("請輸入數值(Q或q代表輸入結束) : ")
    if value == "q" or value == "Q":
        break
    else:
        data.append(int(value))

print(quick_sort_dec(data))























