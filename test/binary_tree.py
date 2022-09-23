class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        pass

    def search(self, val):
        pass

    def inorder(self):
        """後序列印"""
        pass


tree = Node()
value = [10, 5, 3, 65, 21, 88]
for v in value:
    tree.insert(v)

print(tree.search(5))
