package com.fghpdf.KthSmallestElementInABST;


import com.fghpdf.TreeNode;

/**
 * @author fghpdf
 * @date 2019/12/19
 * https://leetcode.com/problems/kth-smallest-element-in-a-bst/
 * count left tree, like binary search tree
 * see https://leetcode.com/problems/kth-smallest-element-in-a-bst/discuss/63660/3-ways-implemented-in-JAVA-(Python)%3A-Binary-Search-in-order-iterative-and-recursive
 **/
public class Solution {
	public int kthSmallest(TreeNode root, int k) {
		int count = countTreeNode(root.left);
		if (k <= count) {
			return kthSmallest(root.left, k);
		} else if (k > count + 1) {
			// 1 is current node
			return kthSmallest(root.right, k - 1 -count);
		}

		return root.val;
	}

	private int countTreeNode(TreeNode root) {
		if (root == null) {
			return 0;
		}

		return 1 + countTreeNode(root.left) + countTreeNode(root.right);
	}
}
