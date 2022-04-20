from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.q = []
        while root:
          self.q.append(root)
          root = root.left

    def next(self) -> int:
        node = self.q.pop()
        r = node.right
        while r:
          self.q.append(r)
          r = r.left
        return node.val

    def hasNext(self) -> bool:
        return self.q

