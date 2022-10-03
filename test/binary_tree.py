class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.data = val

    def insert(self, val):
        # 判斷tree是否為空
        if self.data is None:
            self.data = val
            return
        if val < self.data:
            if not self.left:
                self.left = Node(val)
                return
            self.left.insert(val)
        else:
            if not self.right:
                self.right = Node(val)
                return
            self.right.insert(val)

    def search(self, val):
        if self.data == val:
            return True
        elif val > self.data:
            if not self.right:
                return False
            return self.right.search(val)
        elif val < self.data:
            if not self.left:
                return False
            return self.left.search(val)

    def inorder(self):
        """後序列印"""
        if self.left is not None:
            self.left.inorder()
        if self.right is not None:
            self.right.inorder()
        print(self.data)


data = [10, 5, 3, 65, 21, 88]
tree = Node()
for d in data:
    tree.insert(d)
print(tree.search(88))
tree.inorder()
tree = Node()
value = [10, 5, 3, 65, 21, 88]
for v in value:
    tree.insert(v)

print(tree.search(5))
