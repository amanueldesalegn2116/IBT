"""
Day 09 - Non-Linear Data Structures (BST, Graph, Heap)
"""
from collections import deque

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val: int):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)

    def _insert_recursive(self, node: TreeNode, val: int):
        if val < node.val:
            if not node.left:
                node.left = TreeNode(val)
            else:
                self._insert_recursive(node.left, val)
        else:
            if not node.right:
                node.right = TreeNode(val)
            else:
                self._insert_recursive(node.right, val)

    def inorder(self) -> list:
        res = []
        def _dfs(node):
            if node:
                _dfs(node.left)
                res.append(node.val)
                _dfs(node.right)
        _dfs(self.root)
        return res


class Graph:
    """Graph using Adjacency List."""
    def __init__(self):
        self.adj = {}

    def add_edge(self, u: str, v: str):
        self.adj.setdefault(u, []).append(v)
        self.adj.setdefault(v, [])

    def bfs(self, start: str) -> list:
        visited = set()
        queue = deque([start])
        visited.add(start)
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in self.adj.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order


if __name__ == "__main__":
    bst = BinarySearchTree()
    for item in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(item)
    print("BST Inorder Traversal:", bst.inorder())

    g = Graph()
    g.add_edge("Main Branch", "Addis Hub")
    g.add_edge("Main Branch", "Hawassa Hub")
    g.add_edge("Addis Hub", "Bole Branch")
    g.add_edge("Addis Hub", "Kazanchis Branch")
    print("Graph BFS from Main Branch:", g.bfs("Main Branch"))
