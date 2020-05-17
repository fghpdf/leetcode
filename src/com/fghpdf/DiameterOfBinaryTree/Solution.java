package com.fghpdf.DiameterOfBinaryTree;

/**
 * @author fghpdf
 * @date 2020/5/17
 * @link https://leetcode.com/problems/diameter-of-binary-tree/
 * the max is left max depth + right max depth,
 * so we should get subtree max depth to compare left subtree and right subtree
 **/
public class Solution {
    public int diameterOfBinaryTree(TreeNode root) {
        if (root == null) {
            return 0;
        }

        // left subtree
        int left = diameterOfBinaryTree(root.left);
        // right subtree
        int right = diameterOfBinaryTree(root.right);
        // left + right
        int forsee = getDepthOfBinaryTree(root.left) + getDepthOfBinaryTree(root.right);

        return Math.max(forsee, Math.max(left, right));

    }

    private int getDepthOfBinaryTree(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int leftMaxDepth = getDepthOfBinaryTree(root.left);
        int rightMaxDepth = getDepthOfBinaryTree(root.right);

        return Math.max(leftMaxDepth, rightMaxDepth) + 1;
    }
}
