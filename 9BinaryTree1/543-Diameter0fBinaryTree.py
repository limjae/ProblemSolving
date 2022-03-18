# https://leetcode.com/problems/diameter-of-binary-tree/
from typing import *
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 58 ~ 87ms
class Solution:
    max_length = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def DFS(cur_node):
            left_length = 0
            right_length = 0

            if cur_node.left:
                left_length = 1 + DFS(cur_node.left)
            if cur_node.right:
                right_length = 1 + DFS(cur_node.right)
            self.max_length = max(self.max_length, left_length + right_length)

            return max(left_length, right_length)

        DFS(root)
        return self.max_length

