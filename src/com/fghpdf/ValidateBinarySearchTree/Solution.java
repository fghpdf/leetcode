package com.fghpdf.ValidateBinarySearchTree;

/**
 * @author fghpdf
 * @date 2019/11/30
 * https://leetcode.com/problems/validate-binary-search-tree/
 * use another node to save prev node
 * compare prev <= current
 *
 * summary
 * https://leetcode.com/problems/validate-binary-search-tree/discuss/32112/Learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-(Java-Solution)
 **/
public class Solution {
	private TreeNode prev;

	public boolean isValidBST(TreeNode root) {
		if (root == null) {
			return true;
		}

		if (!isValidBST(root.left)) {
			return false;
		}

		if (prev != null && prev.val >= root.val) {
			return false;
		}

		prev = root;

		return isValidBST(root.right);
	}

}
