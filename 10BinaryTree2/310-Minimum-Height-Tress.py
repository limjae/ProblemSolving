from typing import *
from collections import defaultdict

# Brute Force
class Solution:
    min_height = 0

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = defaultdict(list)
        for link in edges:
            tree[link[0]].append(link[1])
            tree[link[1]].append(link[0])

        visited = []

        def DFS(cur_node):
            visited[cur_node] = True
            length = 0
            for linked in tree[cur_node]:
                if not visited[linked]:
                    length = max(length, DFS(linked))
            return length + 1

        self.min_height = n
        height_dict = defaultdict(list)

        for i in range(n):
            visited = [False for _ in range(n)]
            dfs_height = DFS(i)
            height_dict[dfs_height].append(i)
            self.min_height = min(self.min_height, dfs_height)

        return height_dict[self.min_height]


# Erasing Leaf
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = defaultdict(set)
        nodes = set([i for i in range(n)])
        for link in edges:
            tree[link[0]].add(link[1])
            tree[link[1]].add(link[0])

        leaves = set()
        for node in nodes:
            if len(tree[node]) == 1:
                leaves.add(node)

        while n > 2:
            n -= len(leaves)

            next_leaves = set()

            for leaf in leaves:
                linked = tree[leaf].pop()
                tree[linked].remove(leaf)
                nodes.remove(leaf)

                if len(tree[linked]) == 1:
                    next_leaves.add(linked)

            leaves = next_leaves

        return nodes


