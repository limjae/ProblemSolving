# Definition for a binary tree node.
# 미해결
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    max_index = 0
    def serialize(self, root):
        self.max_index = 0

        def DFS1(node, cur_location):
            if node is not None:
                if node.left:
                    DFS1(node.left, (cur_location + 1) * 2 - 1)
                if node.right:
                    DFS1(node.right, (cur_location + 1) * 2)
            self.max_index = max(self.max_index, cur_location)

        DFS1(root, 0)
        answer = [ None for _ in range(self.max_index + 1)]

        def DFS2(node, cur_location):
            if node is not None:
                if node.left:
                    DFS2(node.left, (cur_location + 1) * 2 - 1)
                if node.right:
                    DFS2(node.right, (cur_location + 1) * 2)
                answer[cur_location] = node.val

        DFS2(root, 0)
        print(answer)
        return answer



    def deserialize(self, data):
        root = TreeNode(data[0])
        length = len(data)
        print(data)

        def DFS3(node, cur_location):
            if node is None:
                return None

            if (cur_location + 1) * 2 - 1 <= length:
                node.left = data[(cur_location + 1) * 2 - 1]
                DFS3(node.left, (cur_location + 1) * 2 - 1)

            if (cur_location + 1) * 2 <= length:
                node.right = data[(cur_location + 1) * 2]
                DFS3(node.right, (cur_location + 1) * 2)

        DFS3(root, 0)

        return root

        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))