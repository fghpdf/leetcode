package com.fghpdf.SameTree;


/**
 * https://leetcode.com/problems/same-tree/
 * @author fghpdf
 */
public class Solution {
	public boolean isSameTree(TreeNode p, TreeNode q) {
		if (p == null && q == null) {
			return true;
		}

		/** now you have two situation
		 * all not null
		 * one of null
		 * and ont of null should return false
		 */
		if (p == null || q == null) {
			return false;
		}

		if (p.val != q.val ) {
			return false;
		}

		return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
	}

}
