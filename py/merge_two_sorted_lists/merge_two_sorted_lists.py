'''
Author: fghpdf
Date: 2021-10-12 09:17:34
LastEditTime: 2021-10-12 09:26:28
LastEditors: fghpdf
'''
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
          return None

        p = ListNode()
        head = p

        while l1 and l2:
          if l1.val < l2.val:
            p.next = l1
            l1 = l1.next
          else:
            p.next = l2
            l2 = l2.next
          
          p = p.next
        
        if l1:
          p.next = l1

        if l2:
          p.next = l2

        return head.next