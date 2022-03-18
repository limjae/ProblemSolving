# https://leetcode.com/problems/longest-univalue-path/
# Definition for a binary tree node.
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_length = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        def DFS(cur_node):
            left_length = 0
            right_length = 0

            if cur_node.left:
                if cur_node.left.val == cur_node.val:
                    left_length = 1 + DFS(cur_node.left)
                else:
                    DFS(cur_node.left)
                    left_length = 0

            if cur_node.right:
                if cur_node.right.val == cur_node.val:
                    right_length = 1 + DFS(cur_node.right)
                else:
                    DFS(cur_node.right)
                    right_length = 0

            self.max_length = max(self.max_length, left_length + right_length)

            return max(left_length, right_length)

        DFS(root)
        return self.max_length












