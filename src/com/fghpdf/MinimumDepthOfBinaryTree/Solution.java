package com.fghpdf.MinimumDepthOfBinaryTree;

/**
 * https://leetcode.com/problems/minimum-depth-of-binary-tree/
 * @author fghpdf
 */
public class Solution {
	public int minDepth(TreeNode root) {
		if (root == null) {
			return 0;
		}

		int left = minDepth(root.left);
		int right = minDepth(root.right);

		// a leaf node is null, so min is another
		if (left == 0 || right == 0) {
			return left + right + 1;
		}

		return Math.min(left, right) + 1;
	}
}
