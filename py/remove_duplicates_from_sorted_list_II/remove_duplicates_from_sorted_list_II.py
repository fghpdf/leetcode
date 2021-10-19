'''
Author: fghpdf
Date: 2021-10-19 08:55:57
LastEditTime: 2021-10-19 09:07:16
LastEditors: fghpdf
'''
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
          return head

        fakeHead = ListNode()
        fakeHead.next = head

        pre = fakeHead
        cur = head

        while cur:
          while cur.next and cur.val == cur.next.val:
            cur = cur.next

          if pre.next == cur:
            pre = pre.next
          else:
            pre.next = cur.next

          cur = cur.next

        return fakeHead.next