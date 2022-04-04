from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
          return head

        headLen = 0
        temp = head
        while temp != None:
          temp = temp.next
          headLen += 1

        fastK = headLen - k

        slow = head
        fast = head
        preSlow = ListNode(-1)
        preSlow.next = slow
        preFast = ListNode(-1)
        preFast.next = fast

        while k-1 > 0:
          preSlow = slow
          slow = slow.next
          k -= 1

        while fastK > 0:
          preFast = fast
          fast = fast.next
          fastK -= 1

        # swap
        fast.val, slow.val = slow.val, fast.val
        
        return head

        

class TestSolution(unittest.TestCase):
    def testSwapNodes(self):
        sol = Solution()
        self.assertEqual(sol.swapNodes(head = [1,2,3,4,5], k = 2), [1,4,3,2,5])
        self.assertEqual(sol.swapNodes(head = [7,9,6,6,7,8,3,0,9,5], k = 5), [7,9,6,6,8,7,3,0,9,5])

if __name__ == '__main__':
    unittest.main()