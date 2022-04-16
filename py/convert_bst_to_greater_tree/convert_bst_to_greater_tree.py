from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
          return root

        self.val = 0
        def visit(root: Optional[TreeNode]):
          if root:
            # right
            visit(root.right)
            # root
            root.val += self.val
            self.val = root.val
            # left
            visit(root.left)
        visit(root)
        return root