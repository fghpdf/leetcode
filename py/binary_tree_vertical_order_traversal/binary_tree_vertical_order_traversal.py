import collections
from typing import List, Optional
from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = collections.defaultdict(list)
        queue = [(root, 0)]
        i = 0
        while i < len(queue):
            node,  x = queue[i]
            i += 1
            if node:
                cols[x].append(node.val)
                queue += (node.left, x-1), (node.right, x+1)
        return [cols[x] for x in sorted(cols)]