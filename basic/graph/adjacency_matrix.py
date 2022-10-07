vertices = ["A", "B", "C", "D", "E"]

adjacencyMatrix = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0],
]


def find_adjacent_nodes(node) -> list:
    adjacency_nodes = []
    index = vertices.index(node)
    edge = adjacencyMatrix[index]
    for i in range(len(edge)):
        if edge[i] == 1:
            adjacency_nodes.append(vertices[i])
    return adjacency_nodes

# is_connect

# time complexity O(v) to find adjacent nodes
# time complexity O(1) to check if two nodes are connected
# space complexity O(v^2)


print(find_adjacent_nodes("C"))
