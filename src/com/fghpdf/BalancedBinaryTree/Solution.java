package com.fghpdf.BalancedBinaryTree;

/**
 * @author fghpdf
 */
public class Solution {
	boolean isBalanced(TreeNode root) {
		if (getDepthByDFS(root) != -1) {
			return true;
		}

		return false;
	}



	/**
	 * can use this method to get left and right depth
	 * but the complexity is O(N^2) in worse case, O(nlogn) is average case
	 * @param root
	 * @return
	 */
	int getDepth(TreeNode root) {
		if (root == null) {
			return 0;
		}

		return Math.max(getDepth(root.left), getDepth(root.right)) + 1;
	}

	int getDepthByDFS(TreeNode root) {
		if (root == null) {
			return 0;
		}

		int leftDepth = getDepthByDFS(root.left);
		if (leftDepth == -1) {
			return -1;
		}
		int rightDepth = getDepthByDFS(root.right);
		if (rightDepth == -1) {
			return -1;
		}

		if (Math.abs(leftDepth - rightDepth) > 1) {
			return -1;
		}

		return Math.max(leftDepth, rightDepth) + 1;
	}
}
