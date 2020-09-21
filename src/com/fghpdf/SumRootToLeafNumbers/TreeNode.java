package com.fghpdf.SumRootToLeafNumbers;

/**
 * @author qxx
 * @date 9/21/2020
 * @link
 **/
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
