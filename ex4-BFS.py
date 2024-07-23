class Node:
    def __init__(self, v, weight):
        self.v = v
        self.weight = weight

class PathNode:
    def __init__(self, node, parent):
        self.node = node
        self.parent = parent

def addEdge(u, v, weight):
    adj[u].append(Node(v, weight))

def GBFS(h, V, src, dest):
    openList = []
    closeList = []
    openList.append(PathNode(src, None))

    while openList:
        currentNode = openList.pop(0)
        closeList.append(currentNode)

        if currentNode.node == dest:
            path = []
            cur = currentNode
            while cur:
                path.append(cur.node)
                cur = cur.parent
            path.reverse()
            return path

        for node in adj[currentNode.node]:
            if any(node.v == x.node for x in openList) or any(node.v == x.node for x in closeList):
                continue
            openList.append(PathNode(node.v, currentNode))

    return []

# Example usage:
V = 10
adj = [[] for _ in range(V)]

addEdge(0, 1, 2)
addEdge(0, 2, 1)
addEdge(0, 3, 10)
addEdge(1, 4, 3)
addEdge(1, 5, 2)
addEdge(2, 6, 9)
addEdge(3, 7, 5)
addEdge(3, 8, 2)
addEdge(7, 9, 5)

h = [20, 22, 21, 10, 25, 24, 30, 5, 12, 0]

path = GBFS(h, V, 0, 9)

if path:
    print("Shortest Path found:", ' -> '.join(map(str, path)))
else:
    print("No path found from src to dest")
