class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        return self.goodRoot(root, -100000)

    def goodRoot(self, root: TreeNode, maxVal: int) -> int:
        if not root:
          return 0

        count = 0
        if root.val >= maxVal:
          count += 1

        count += self.goodRoot(root.left, max(maxVal, root.val))
        count += self.goodRoot(root.right, max(maxVal, root.val))

        return count