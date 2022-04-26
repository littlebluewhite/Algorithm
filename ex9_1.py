# ex9_1.py
def bubble_sort(nLst):
    length = len(nLst)
    for i in range(length-1):
        print("第 %d 次外圈排序" % (i+1))
        for j in range(length-1-i):
            if nLst[j] < nLst[j+1]:
                nLst[j],nLst[j+1] = nLst[j+1],nLst[j]
            print("第 %d 次內圈排序 : " % (j+1), nLst)
    return nLst

data = [6, 1, 5, 7, 3]
print("原始串列 : ", data)
print("排序結果 : ", bubble_sort(data))





def sort_des(l1:list):
    n = len(l1)
    for i in range(n-1):
        for j in range(n-1-i):
            if l1[j] < l1[j+1]:
                l1[j], l1[j+1] = l1[j+1], l1[j]
    return l1

print(sort_des(data))






