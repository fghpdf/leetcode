class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        self.res = TreeNode(-1)
        head = self.res
        def inorder(root: TreeNode):
            if not root:
                return
            inorder(root.left)
            self.res.right = TreeNode(root.val)
            self.res = self.res.right
            inorder(root.right)
        inorder(root)
        return head.right