'''
Author: fghpdf
Date: 2022-01-11 09:16:52
LastEditTime: 2022-01-11 09:24:54
LastEditors: fghpdf
'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inOrder(root: TreeNode):
            if not root:
                return []
            sortedArray = []
            sortedArray.extend(inOrder(root.left))
            sortedArray.append(root)
            sortedArray.extend(inOrder(root.right))

            return sortedArray

        def sortedArrayToBST(sortedArray: List[TreeNode], left: int, right: int) -> TreeNode:
            if left > right:
                return None

            mid = (left + right) // 2
            root = sortedArray[mid]
            root.left = sortedArrayToBST(sortedArray, left, mid-1)
            root.right = sortedArrayToBST(sortedArray, mid, right)

            return root

        sortedArray = inOrder(root)
        return sortedArrayToBST(sortedArray, 0, len(sortedArray) - 1)

