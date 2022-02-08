'''
Author: fghpdf
Date: 2022-02-08 09:10:26
LastEditTime: 2022-02-08 09:25:48
LastEditors: fghpdf
'''
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.height(root, res)
        return res

    def height(self, root: Optional[TreeNode], res: List[List[int]]):
        if not root:
          return -1
        
        level = 1 + max(self.height(root.left, res), self.height(root.right, res))
        if len(res) < level+1:
            res.append([])
        res[level].append(root.val)
        
        return level
