package com.fghpdf.ConvertSortedArrayToBinarySearchTree;

/**
 * https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
 * @author fghpdf
 * use dichotomy to insert tree node
 */
class Solution {
	public TreeNode sortedArrayToBST(int[] nums) {
		if (nums.length == 0) {
			return null;
		}

		TreeNode head = insertBSTNode(nums, 0, nums.length - 1);
		return head;
	}

	public TreeNode insertBSTNode(int[] nums, int left, int right) {
		if (left > right) {
			return null;
		}

		int mid = (left + right) / 2;

		// root node
		TreeNode treeNode = new TreeNode(nums[mid]);
		treeNode.left = insertBSTNode(nums, left, mid - 1);
		treeNode.right = insertBSTNode(nums, mid + 1, right);
		return treeNode;
	}
}
