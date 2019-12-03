package com.fghpdf.PopulatingNextRightPointersInEachNode;

/**
 * @author fghpdf
 * @date 2019/12/3
 * https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
 * connect left->right
 * and two node's son
 **/
public class Solution {
	public Node connect(Node root) {
		if (root == null || root.left == null) {
			return root;
		}
		connectNodes(root.left, root.right);
		return root;
	}

	private void connectNodes(Node a, Node b) {
		a.next = b;
		if (a.left != null) {
			connectNodes(a.right, b.left);
			connectNodes(a.left, a.right);
			connectNodes(b.left, b.right);
		}
	}
}
