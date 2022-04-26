# ex7_1.py
import heapq

h_list = [10, 21, 5, 9, 13, 28, 3]
h = []
for i in range(len(h_list)):
    heapq.heappush(h, h_list[i])
    print("插入 {0:2d} 後的二元堆積樹 h = {1}".format(h_list[i], h))


