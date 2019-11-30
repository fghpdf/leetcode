package com.fghpdf.BinaryTreeInorderTraversal;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/**
 * @author fghpdf
 * @date 2019/11/30
 * https://leetcode.com/problems/binary-tree-inorder-traversal/
 * inorder is left -> root -> right
 * three ways to solve this problem
 * 1. Recursive O(n) time and O(n) space
 * 2. Iterative using stack O(n) time and O(n) space
 * 3. Morris traversal O(n) time and O(1) space
 * Morris makes current node's left tree's rightest node's right point is current node
 *
 **/
public class Solution {
	public List<Integer> inorderTraversal(TreeNode root) {
		List<Integer> result = new ArrayList<>();

		if (root == null) {
			return result;
		}

		result.addAll(inorderTraversal(root.left));
		result.add(root.val);
		result.addAll(inorderTraversal(root.right));

		return result;
	}

	private List<Integer> iterative(TreeNode root) {
		List<Integer> result = new ArrayList<>();
		Stack<TreeNode> todo = new Stack<>();

		while (true) {
			while (root != null) {
				todo.push(root);
				root = root.left;
			}

			if (todo.isEmpty()) {
				break;
			}

			root = todo.pop();
			result.add(root.val);
			root = root.right;
		}

		return result;
	}

	private List<Integer> mirrors(TreeNode root) {
		List<Integer> result = new ArrayList<>();

		while (root != null) {
			if (root.left != null) {
				TreeNode mirror = root.left;
				while (mirror.right != null && mirror != root) {
					mirror = mirror.right;
				}

				if (mirror.right == null) {
					mirror.right = root;
					root = root.left;
				} else {
					mirror.right = null;
					result.add(root.val);
					root = root.right;
				}
			} else {
				result.add(root.val);
				root = root.right;
			}
		}

		return result;
	}
}
