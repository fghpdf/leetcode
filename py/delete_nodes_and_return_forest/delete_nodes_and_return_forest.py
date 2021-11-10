from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        self.helper(root, to_delete, res, False)
        return res
    def helper(self, root: TreeNode, to_delete: List[int], res: List[TreeNode], parent_exist: bool):
        if root == None:
            return None

        if root.val in to_delete:
          root.left = self.helper(root.left, to_delete, res, False)
          root.right = self.helper(root.right, to_delete, res, False)
          return None
        else:
          if not parent_exist:
            res.append(root)
          root.left = self.helper(root.left, to_delete, res, True)
          root.right = self.helper(root.right, to_delete, res, True)
          return root

        