package com.fghpdf.BinaryTreeLevelOrderTraversal;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * @author fghpdf
 * @date 2019/12/1
 **/
public class Solution {
	public List<List<Integer>> levelOrder(TreeNode root) {
		List<List<Integer>> result = new LinkedList<>();
		Queue<TreeNode> levelNodes = new LinkedList<>();

		if (root == null) {
			return result;
		}

		levelNodes.offer(root);
		while (!levelNodes.isEmpty()) {
			int level = levelNodes.size();
			List<Integer> row = new LinkedList<>();
			for (int i = 0; i < level; i++) {
				TreeNode levelNode = levelNodes.peek();
				if (levelNode == null) {
					continue;
				}

				if (levelNode.left != null) {
					levelNodes.offer(levelNode.left);
				}

				if (levelNode.right != null) {
					levelNodes.offer(levelNode.right);
				}
				row.add(levelNode.val);
				levelNodes.poll();
			}
			result.add(row);
		}
		return result;
	}
}
