package com.fghpdf.LowestCommonAncestorOfABinaryTree;

import com.fghpdf.TreeNode;

/**
 * @author fghpdf
 * @date 2019/12/21
 * https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
 * the lowest common ancestor for a tree must be children ancestor
 **/
public class Solution {
	public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
		if (root == null || root == p || root == q) {
			return root;
		}

		TreeNode left = lowestCommonAncestor(root.left, p, q);
		TreeNode right = lowestCommonAncestor(root.right, p, q);
		if (left == null) {
			return right;
		}

		if (right == null) {
			return left;
		}

		return root;
	}
}
