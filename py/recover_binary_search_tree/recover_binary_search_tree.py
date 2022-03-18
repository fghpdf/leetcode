from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        swap = [None, None]
        self.prev = TreeNode(float('-inf'))
        def dfs(node: Optional[TreeNode]):
            if node:
                dfs(node.left)
                if node.val < self.prev.val:
                    if not swap[0]: swap[0] = self.prev
                    swap[1] = node
                self.prev = node
                dfs(node.right)
        dfs(root)
        swap[0].val, swap[1].val = swap[1].val, swap[0].val