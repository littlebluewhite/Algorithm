from typing import Any


class Graph:

    def __init__(self):
        self.vertices = ["A", "B", "C", "D", "E"]
        self.edges: list[list] = [
            ["A", "B"],
            ["A", "D"],
            ["B", "C"],
            ["C", "D"],
            ["C", "E"],
            ["D", "E"],
        ]

    def find_adjacent_nodes(self, node):
        adjacent_nodes: list = []

        for edge in self.edges:
            if node in edge:
                idx = edge.index(node)
                if idx == 0:
                    adjacent_nodes.append(edge[1])
                else:
                    adjacent_nodes.append(edge[0])
        return adjacent_nodes

    def is_connect(self, node1, node2) -> bool:
        for edge in self.edges:
            if node1 in edge and node2 in edge:
                return True
        return False


test = Graph()
print(test.find_adjacent_nodes("C"))
print(test.is_connect("A", "E"))
