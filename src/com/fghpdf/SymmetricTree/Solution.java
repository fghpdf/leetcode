package com.fghpdf.SymmetricTree;

import java.util.Stack;

/**
 * https://leetcode.com/problems/symmetric-tree/
 * @author fghpdf
 * can use Recursive or stack to work out this problem
 * stack is push left.left, right.right, left.right, right.left
 * and then compare val
 */
public class Solution {
	public boolean isSymmetric(TreeNode root) {
		if (root == null) {
			return true;
		}

		return compareTwoNode(root.left, root.right);
	}

	/**
	 * Recursive
	 * @param left
	 * @param right
	 * @return
	 */
	public boolean compareTwoNode(TreeNode left, TreeNode right) {
		if (left == null || right == null) {
			return left == right;
		}

		if (left.val != right.val) {
			return false;
		}

		return compareTwoNode(left.left, right.right) && compareTwoNode(left.right, right.left);
	}

	public boolean compareWithStack(TreeNode root) {
		if (root == null) {
			return true;
		}

		Stack<TreeNode> treeStack = new Stack<>();
		treeStack.push(root.left);
		treeStack.push(root.right);

		while (!treeStack.isEmpty()) {
			TreeNode left = treeStack.pop();
			TreeNode right = treeStack.pop();

			if (left == null && right == null) {
				continue;
			}

			if (left == null || right == null ||
					left.val != right.val) {
				return false;
			}

			treeStack.push(left.left);
			treeStack.push(right.right);
			treeStack.push(left.right);
			treeStack.push(right.left);
		}

		return true;
	}
}
