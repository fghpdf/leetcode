from typing import AnyStr, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    ans = 0
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        self.distribute(root)
        return self.ans

    def distribute(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        left = self.distribute(root.left)
        right = self.distribute(root.right)
        self.ans += abs(left) + abs(right)
        return root.val + left + right - 1
