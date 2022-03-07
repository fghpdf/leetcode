from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
      if root == None:
        return ""

      def find(root: Optional[TreeNode], target: int, path: List[int]) -> bool:
        if root.val == target:
          return True
        if root.left and find(root.left, target, path):
          path += "L"
        elif root.right and find(root.right, target, path):
          path += "R"
        return path
      
      s, d = [], []
      find(root, startValue, s)
      find(root, destValue, d)

      # remove the prefix
      while len(s) and len(d) and s[-1] == d[-1]:
        s.pop()
        d.pop()
      return "".join("U"*len(s)) + "".join(reversed(d))

