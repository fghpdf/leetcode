'''
Author: fghpdf
Date: 2021-10-23 10:44:51
LastEditTime: 2021-10-23 11:03:37
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
      while root:
        cur = temp = Node()
        while root:
          if root.left:
            cur.next = root.left
            cur = cur.next

          if root.right:
            cur.next = root.right
            cur = cur.next
          root = root.next
        root = temp.next

      return head
      