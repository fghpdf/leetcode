'''
Author: fghpdf
Date: 2021-10-23 11:49:33
LastEditTime: 2021-10-23 12:05:17
LastEditors: fghpdf
'''
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
          return False

        if self.isSame(root, subRoot):
          return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
      if root == None or subRoot == None:
        return root == subRoot

      if root.val != subRoot.val:
        return False

      return self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right)