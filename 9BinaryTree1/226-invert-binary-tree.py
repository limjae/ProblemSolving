# https://leetcode.com/problems/invert-binary-tree/
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        def DFS(cur_node):
            if cur_node.left:
                DFS(cur_node.left)
            if cur_node.right:
                DFS(cur_node.right)

            cur_node.left, cur_node.right = cur_node.right, cur_node.left

        DFS(root)

        return root


