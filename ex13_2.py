# ex13_2.py                 
def dfs(graph, start, goal):
    ''' 深度優先搜尋法 '''
    path = []                               # 拜訪過的節點
    stack = [start]                         # 模擬堆疊
    while stack:        
        node = stack.pop()                  # pop堆疊
        if node in path:
            continue
        path.append(node)                   # 加入已拜訪行列
        if node == goal:                    # 如果找到了
            print('找到了')
            return path
        for n in graph[node]:               # 將相鄰節點放入佇列
            stack.append(n)
    return "找不到"

graph = {'A':['B', 'C', 'D'],
         'B':['A', 'E'],
         'C':['A', 'F'],
         'D':['A', 'G', 'H'],
         'E':['B'],
         'F':['C', 'I', 'J'],
         'G':['D'],
         'H':['D'],
         'I':['F'],
         'J':['F']
        }
print(dfs(graph,'F','G'))









































def depth_first_search(init, target):
    searched_list = []
    stack = [init]
    while stack:
        item = stack.pop()
        searched_list.append(item)
        if item == target:
            print("Find")
            print(searched_list)
        else:
            for i in graph[item]:
                if i not in searched_list:
                    stack.append(i)

depth_first_search("C", "G")

# graph = {'A':['B', 'C', 'D'],
#          'B':['A', 'E'],
#          'C':['A', 'F'],
#          'D':['A', 'G', 'H'],
#          'E':['B'],
#          'F':['C', 'I', 'J'],
#          'G':['D'],
#          'H':['D'],
#          'I':['F'],
#          'J':['F']
#         }







