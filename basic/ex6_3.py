# ex6_3.py
class Node():
    def __init__(self, data=None):
        ''' 建立二元樹的節點 '''
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        ''' 建立二元樹 '''
        if self.data:                           # 如果根節點存在
            if data < self.data:                # 插入值小於目前節點值
                if self.left:
                    self.left.insert(data)      # 遞迴呼叫往下一層
                else:
                    self.left = Node(data)      # 建立新節點存放資料
            else:                               # 插入值大於目前節點值
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)                
        else:                                   # 如果根節點不存在
            self.data = data                    # 建立根節點

    def postorder(self):
        ''' 後序列印 '''                      
        if self.left:                           # 如果左子節點存在
            self.left.postorder()               # 遞迴呼叫下一層        
        if self.right:                          # 如果右子節點存在
            self.right.postorder()              # 遞迴呼叫下一層
        print(self.data)                        # 列印

class Delete_Node():
    def deleteNode(self, root, key):
        if root is None:                        # 二元樹不存在返回
            return None

        if key < root.data:                     # 刪除值小於root值則往左
            root.left = self.deleteNode(root.left, key)
            return root

        if key > root.data:                     # 刪除值大於root值則往右
            root.right = self.deleteNode(root.right, key)
            return root

        if root.left is None:                   # 左邊節點不存在
            new_root = root.right
            root.right = None
            return new_root

        if root.right is None:                  # 右邊節點不存在
            new_root = root.left
            root.left = None
            return new_root

        succ = self.min_node(root.right)        # 找右子樹中最小值的節點
        tmp = Node(succ.data)                   # 用此最大值建立節點
        tmp.left = root.left                    # 串接原刪除節點的左子樹
        tmp.right = self.right_node(root.right) # 節點串接原刪除節點的右子樹
        root.left = None
        root.right = None
        return tmp

    def right_node(self, node):
        ''' 找出原刪除節點左子樹 '''
        if node.left is None:                   # 左子節點不存在
            new_root = node.right               # 使用右子節點
            node.right = None
            return new_root
        node.left = self.right_node(node.left)  # 進入下一層
        return node

    def min_node(self, node):
        '''  找尋最小值節點 '''
        while node.left:                       # 如果是否則node是最小值節點
            node = node.left
        return node
        
tree = Node()                                   # 建立二元樹物件
datas = [10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32] # 建立二元樹數據
for d in datas:
    tree.insert(d)                              # 分別插入數據
tree.postorder()                                # 後序列印
del_data = 10
print("刪除 %d 資料後" % del_data)
delete_obj = Delete_Node()                      # 建立刪除節點物件
result = delete_obj.deleteNode(tree, del_data)  # 刪除操作
result.postorder()                              # 後序列印



    

class Node2:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node2(data)
            if data > self.data:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node2(data)
        else:
            self.data = data

    def postorder_print(self):
        if self.left:
            self.left.postorder_print()
        if self.right:
            self.right.postorder_print()
        print(self.data)


class DeleteOperate:
    def delete_node_left_max(self, node, data):
        if node is None:
            return None
        if data < node.data:
            node.left = self.delete_node_left_max(node.left, data)
            return node
        elif data > node.data:
            node.right = self.delete_node_left_max(node.right, data)
            return node
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        num = self.search_max_node(node.left).data
        tmp = Node2(num)
        tmp.left = self.left_node(node.left)
        tmp.right = node.right
        return tmp

    def search_max_node(self, node):
        while node.right:
            node = node.right
        return node

    def left_node(self, node):
        if node.right is None:
            return node.left
        node.right = self.left_node(node.right)
        return node

    def delete_node_right_min(self, node, data):
        if node is None:
            return None
        if data < node.data:
            node.left = self.delete_node_right_min(node.left, data)
            return node
        elif data > node.data:
            node.right = self.delete_node_right_min(node.right, data)
            return node
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        num = self.search_min_node(node.right).data
        tmp = Node2(num)
        tmp.right = self.right_node(node.right)
        tmp.left = node.left
        return tmp

    def search_min_node(self, node):
        while node.left:
            node = node.left
        return node

    def right_node(self, node):
        if node.left is None:
            return node.right
        node.left = self.right_node(node.left)
        return node



print("------------------------------------------------------")
data_list = [10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32]
tree = Node2()
for datum in data_list:
    tree.insert(datum)
tree.postorder_print()

delete_operate = DeleteOperate()
result = delete_operate.delete_node_right_min(tree, 10)
print("------------------------------------------------------")
result.postorder_print()































