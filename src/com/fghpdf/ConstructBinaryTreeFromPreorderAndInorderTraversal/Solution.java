package com.fghpdf.ConstructBinaryTreeFromPreorderAndInorderTraversal;

import java.util.HashMap;
import java.util.Map;

/**
 * @author fghpdf
 * @date 2019/12/2
 * https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
 * the pre order first element is root
 * search root element in order, left is left sub tree, right is right sub tree
 **/
public class Solution {
	public TreeNode buildTree(int[] preorder, int[] inorder) {
		Map<Integer, Integer> inMap = new HashMap<>(16);

		for (int i = 0; i < inorder.length; i++) {
			inMap.put(inorder[i], i);
		}


		return builder(preorder, 0, preorder.length - 1, inorder, 0, inorder.length - 1, inMap);
	}

	private TreeNode builder(int[] preOrder, int preStart, int preEnd, int[] inOrder, int inStart, int inEnd, Map<Integer, Integer> inMap) {
		if (preStart > preEnd || inStart > inEnd) {
			return null;
		}

		TreeNode root = new TreeNode(preOrder[preStart]);
		int inRoot = inMap.get(root.val);
		int numsLeft = inRoot - inStart;

		root.left = builder(preOrder, preStart + 1, preStart + numsLeft, inOrder, inStart, inRoot - 1, inMap);
		root.right = builder(preOrder, preStart + numsLeft + 1, preEnd, inOrder, inRoot + 1, inEnd, inMap);

		return root;
	}
}
