from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
          return None

        if not head.next:
          return TreeNode(head.val)

        # find middle point
        fast = head.next.next
        slow = head
        while fast and fast.next:
          fast = fast.next.next
          slow = slow.next

        tmp = slow.next
        slow.next = None
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)

        return root