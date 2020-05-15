package com.fghpdf.InvertBinaryTree;

/**
 * @author fghpdf
 * @date 2020/5/15
 * @link https://leetcode.com/problems/invert-binary-tree/
 * just left to right and right to left
 **/
public class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return null;
        }
        // left
        TreeNode left = invertTree(root.left);
        // right
        TreeNode right = invertTree(root.right);

        // invert
        root.left = right;
        root.right = left;
        return root;
    }
}
