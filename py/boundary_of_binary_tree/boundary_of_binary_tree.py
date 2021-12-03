# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    nodes: List[int]

    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        self.nodes = []

        if root == None:
            return self.nodes
        self.nodes.append(root.val)
        self.leftBoundary(root.left)
        self.leaves(root.left)
        self.leaves(root.right)
        self.rightBoundary(root.right)

        return self.nodes

    def leftBoundary(self, root: Optional[TreeNode]):
        if root == None or (root.left == None and root.right == None):
            return
        # all left is boundary
        self.nodes.append(root.val)
        if root.left == None:
          self.leftBoundary(root.right)
        else:
          self.leftBoundary(root.left)

    def rightBoundary(self, root: Optional[TreeNode]):
        if root == None or (root.left == None and root.right == None):
            return
        if root.right == None:
            self.rightBoundary(root.left)
        else:
            self.rightBoundary(root.right)
        # reverse visit all children
        self.nodes.append(root.val)

    def leaves(self, root: Optional[TreeNode]):
        if root == None:
            return
        self.leaves(root.left)
        if root.left == None and root.right == None:
            # leaf
            self.nodes.append(root.val)
            return
        self.leaves(root.right)