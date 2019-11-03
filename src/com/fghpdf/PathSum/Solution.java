package com.fghpdf.PathSum;

/**
 * https://leetcode.com/problems/path-sum/
 * @author fghpdf
 */
public class Solution {
	public boolean hasPathSum(TreeNode root, int sum) {
		if (root == null) {
			return false;
		}

		// the leaf node whose sum is 0 should be true
		if (root.right == null && root.left == null && sum - root.val == 0) {
			return true;
		}

		return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);
	}
}
