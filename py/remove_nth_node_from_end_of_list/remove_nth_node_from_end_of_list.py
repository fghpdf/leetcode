'''
Author: fghpdf
Date: 2021-10-07 09:56:24
LastEditTime: 2021-10-07 10:04:40
LastEditors: fghpdf
'''
from typing import Optional
from py.helper import ListNode
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      # fast can be n
      # slow is the pre pointer of delete node
      fast = head
      slow = head
      step = n
      while step != 0:
        fast = fast.next
        step -= 1

      if fast == None:
        return head.next
      
      while fast != None:
        fast = fast.next
        slow = slow.next

      slow.next = slow.next.next
      return head