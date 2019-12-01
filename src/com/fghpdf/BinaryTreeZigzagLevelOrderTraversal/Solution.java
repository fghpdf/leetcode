package com.fghpdf.BinaryTreeZigzagLevelOrderTraversal;

import java.io.IOException;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * @author fghpdf
 * @date 2019/12/1
 * https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
 * I just change https://leetcode.com/problems/binary-tree-level-order-traversal/ Solution
 * add a judgement whether row is odd
 **/
public class Solution {
	public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
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
			if (result.size() % 2 == 1) {
				Collections.reverse(row);
			}
			result.add(row);
		}
		return result;
	}
}

class MainClass {
	public static TreeNode stringToTreeNode(String input) {
		input = input.trim();
		input = input.substring(1, input.length() - 1);
		if (input.length() == 0) {
			return null;
		}

		String[] parts = input.split(",");
		String item = parts[0];
		TreeNode root = new TreeNode(Integer.parseInt(item));
		Queue<TreeNode> nodeQueue = new LinkedList<>();
		nodeQueue.add(root);

		int index = 1;
		while(!nodeQueue.isEmpty()) {
			TreeNode node = nodeQueue.remove();

			if (index == parts.length) {
				break;
			}

			item = parts[index++];
			item = item.trim();
			if (!item.equals("null")) {
				int leftNumber = Integer.parseInt(item);
				node.left = new TreeNode(leftNumber);
				nodeQueue.add(node.left);
			}

			if (index == parts.length) {
				break;
			}

			item = parts[index++];
			item = item.trim();
			if (!item.equals("null")) {
				int rightNumber = Integer.parseInt(item);
				node.right = new TreeNode(rightNumber);
				nodeQueue.add(node.right);
			}
		}
		return root;
	}

	public static String integerArrayListToString(List<Integer> nums, int length) {
		if (length == 0) {
			return "[]";
		}

		String result = "";
		for(int index = 0; index < length; index++) {
			Integer number = nums.get(index);
			result += Integer.toString(number) + ", ";
		}
		return "[" + result.substring(0, result.length() - 2) + "]";
	}

	public static String integerArrayListToString(List<Integer> nums) {
		return integerArrayListToString(nums, nums.size());
	}

	public static String int2dListToString(List<List<Integer>> nums) {
		StringBuilder sb = new StringBuilder("[");
		for (List<Integer> list: nums) {
			sb.append(integerArrayListToString(list));
			sb.append(",");
		}

		sb.setCharAt(sb.length() - 1, ']');
		return sb.toString();
	}

	public static void main(String[] args) throws IOException {
		String line = "[1,2,3,4,null,null,5]";
		TreeNode root = stringToTreeNode(line);

		List<List<Integer>> ret = new Solution().zigzagLevelOrder(root);

		String out = int2dListToString(ret);

		System.out.print(out);
	}
}
