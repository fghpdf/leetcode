package com.fghpdf.BinaryTreeLevelOrderTraversalII;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
 * @author fghpdf
 */
public class Solution {
	public List<List<Integer>> levelOrderBottom(TreeNode root) {
		List<List<Integer>> result = new LinkedList<>();
		dfs(root, 0, result);
		return result;
	}

	public void dfs(TreeNode root, int level, List<List<Integer>> result) {
		if (root == null) {
			return;
		}

		// bottom-up
		if (level >= result.size()) {
			result.add(0, new LinkedList<>());
		}


		if (root.left != null) {
			dfs(root.left, level + 1, result);
		}

		if (root.right != null) {
			dfs(root.right, level + 1, result);
		}

		/**
		 * actually the list add is from bottom start
		 */
		result.get(result.size() - level - 1).add(root.val);
	}

	public void bfs(TreeNode root, List<List<Integer>> result) {
		Queue<TreeNode> queue = new LinkedList<>();

		if (root == null) {
			return;
		}

		queue.offer(root);
		while (!queue.isEmpty()) {
			int levelNum = queue.size();
			List<Integer> subList = new LinkedList<>();
			for (int i = 0; i < levelNum;i++) {
				if (queue.peek().left != null) {
					queue.offer(queue.peek().left);
				}

				if (queue.peek().right != null) {
					queue.offer(queue.peek().right);
				}

				subList.add(queue.poll().val);
			}

			result.add(0, subList);
		}
	}
}
