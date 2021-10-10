'''
Author: fghpdf
Date: 2021-10-10 16:53:15
LastEditTime: 2021-10-10 17:07:50
LastEditors: fghpdf
'''
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
      if root == None:
        return root

      head = root

      while root and root.left:
        # save next root
        next = root.left
        while root:
          # left tree: left -> right
          root.left.next = root.right
          # left tree: right -> right tree: left (perfect)
          root.right.next = root.next and root.next.left
          # change to right tree
          root = root.next
        root = next

      return head
