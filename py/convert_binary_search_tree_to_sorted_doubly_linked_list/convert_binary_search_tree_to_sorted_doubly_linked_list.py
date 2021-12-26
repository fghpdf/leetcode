from typing import Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        head = Node(0)
        prev = head
        stack, node = [], root
        while stack or node:
            # inorder
            # find the leftest node
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            node.left, prev.right, prev = prev, node, node
            # right
            node = node.right
        head.right.left, prev.right = prev, head.right
        return head.right
        