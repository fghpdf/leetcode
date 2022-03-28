from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
      if not head:
        return None

      p = ListNode(-1)
      p.next = head

      curr = p
      while curr.next:
        if curr.next.val == val:
          curr.next = curr.next.next
        else:
          curr = curr.next

      return p.next