# ex9_2.py
import random


def selection_sort(nLst):
    ''' 選擇排序 '''
    for i in range(len(nLst)-1):        
        index = i                           # 最小值的索引
        for j in range(i+1, len(nLst)):     # 找最小值的索引
            if nLst[index][1] < nLst[j][1]:
                index = j
        if i == index:                      # 如果目前索引是最小值索引
            pass                            # 不更動
        else:
            nLst[i],nLst[index] = nLst[index],nLst[i]   # 資料對調
    return nLst

program = [('Python', 98789),
         ('C', 56532),
         ('C#', 88721),
         ('Java', 90397),
         ('C++', 63122),
         ('PHP', 58000)
         ]
         
print("程式語言使用率排行")
selection_sort(program)
for i in range(len(program)):
    print("{0}:{1:7s} -- 使用次數 {2}".format(i+1, program[i][0], program[i][1]))












program = [('Python', 98789),
         ('C', 56532),
         ('C#', 88721),
         ('Java', 90397),
         ('C++', 63122),
         ('PHP', 58000)
         ]


def random_sort_dec(l1):
    if len(l1) <= 1:
        return l1

    left = []
    right = []
    piv = []
    target = random.choice(l1)
    for item in l1:
        if item[1] == target[1]:
            piv.append(item)
        elif item[1] > target[1]:
            right.append(item)
        elif item[1] < target[1]:
            left.append(item)
    return random_sort_dec(right) + piv + random_sort_dec(left)

print(random_sort_dec(program))





def selection_sort_dec(l1):
    for i in range(len(l1)-1):
        max_index = i
        for j in range(i+1, len(l1)):
            if l1[j][1] > l1[max_index][1]:
                max_index = j
        l1[i], l1[max_index] = l1[max_index], l1[i]
    return l1

print(selection_sort_dec(program))
































    
