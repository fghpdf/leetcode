package com.fghpdf.MaximumDepthOfBinaryTree;

/**
 * https://leetcode.com/problems/maximum-depth-of-binary-tree/
 * @author fghpdf
 *
 */
public class Solution {
//	public int maxDepth(TreeNode root) {
//		return getSideDepth(root, 0);
//	}

	public int getSideDepth(TreeNode root, int depth) {
		if (root == null) {
			return depth;
		}

		if (root.right == null && root.left == null) {
			return depth + 1;
		}

		depth++;

		return Math.max(getSideDepth(root.right, depth), getSideDepth(root.left, depth));
	}

	/**
	 * more clear solution
	 * @param root
	 * @return
	 */
	public int maxDepth(TreeNode root) {
		/**
		 * leaf node
		 */
		if (root == null) {
			return 0;
		}

		return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
	}
}
