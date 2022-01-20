'''
Author: fghpdf
Date: 2022-01-20 09:14:38
LastEditTime: 2022-01-20 09:21:39
LastEditors: fghpdf
'''
import collections
from typing import List
import unittest

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
      if not root:
          return []

      conn = collections.defaultdict(list)
      def connect(parent: TreeNode, child: TreeNode):
          if parent and child:
              conn[parent.val].append(child.val)
              conn[child.val].append(parent.val)
          # inorder
          if child.left:
            connect(child, child.left)
          if child.right:
            connect(child, child.right)
      connect(None, root)
      bfs = [target.val]
      seen = set(bfs)
      for i in range(k):
          newLevel = []
          for nodeVal in bfs:
            for connectedNodeVal in conn[nodeVal]:
              if connectedNodeVal not in seen:
                newLevel.append(connectedNodeVal)
          bfs = newLevel
          # add all the values in bfs into seen
          seen |= set(bfs)
      return bfs