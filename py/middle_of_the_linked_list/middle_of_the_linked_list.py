'''
Author: fghpdf
Date: 2021-10-07 09:21:31
LastEditTime: 2021-10-07 09:45:39
LastEditors: fghpdf
'''
from typing import Optional
import unittest

from py.helper import ListNode

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
      # find middle use fast and slow pointer
      fast = head
      slow = head
      # fast arrive at tail
      while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
      
      return slow

class TestMiddleNode(unittest.TestCase):
  def test_middle_node(self):
    sol = Solution()
    self.assertEqual(sol.middleNode())
