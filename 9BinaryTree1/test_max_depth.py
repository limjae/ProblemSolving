from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_tree_by(lst, idx):
    parent = None
    if idx < len(lst):
        value = lst[idx]
        if value is None:
            return

        parent = TreeNode(value)
        parent.left = make_tree_by(lst, 2 * idx + 1)
        parent.right = make_tree_by(lst, 2 * idx + 2)

    return parent

# 수정###
def printq(q):
    for i in q:
        print(i.val, end=" ")
    print()


def test_max_depth(lst):
    root = make_tree_by(lst, 0)

    if not root:
        return 0
    # 수정###
    print(root.val)

    q = deque([root])
    depth = 0
    # 수정###
    printq(q)
    while q:
        depth += 1
        for _ in range(len(q)):
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        # 수정###
        printq(q)

    return depth


assert test_max_depth(lst=[]) == 0
assert test_max_depth(lst=[3, 9, 20, None, None, 15, 7]) == 3