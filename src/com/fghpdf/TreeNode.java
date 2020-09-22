package com.fghpdf;

/**
 * @author fghpdf
 * @date 2019/12/19
 **/
public class TreeNode {
	public int val;
	public TreeNode left;
    public TreeNode right;
    public TreeNode(int x) { val = x; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
