'''
Author: fghpdf
Date: 2021-10-12 09:32:12
LastEditTime: 2021-10-12 09:38:46
LastEditors: fghpdf
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None

        while head:
          temp = head.next
          head.next = tail
          tail = head
          head = temp

        return tail
