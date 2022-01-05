'''
Author: fghpdf
Date: 2022-01-05 09:17:57
LastEditTime: 2022-01-05 09:20:13
LastEditors: fghpdf
'''
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        res = 0
        if root.val >= low and root.right <= high:
            res += root.val
        res += self.rangeSumBST(root.left, low, high)
        res += self.rangeSumBST(root.right, low, high)

        return res
