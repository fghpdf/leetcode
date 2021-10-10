'''
Author: fghpdf
Date: 2021-10-10 15:23:15
LastEditTime: 2021-10-10 16:34:28
LastEditors: fghpdf
'''
from typing import Optional
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
      if root1 and root2:
        root = TreeNode()
        root.val = root1.val + root2.val
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)
        return root
      else:
        return root1 or root2


class TestMergeTrees(unittest.TestCase):
    def test_merge_trees(self):
      sol = Solution()
      self.assertEqual(sol.mergeTrees())

