package com.fghpdf.SumRootToLeafNumbers;

/**
 * @author qxx
 * @date 9/21/2020
 * @link https://leetcode.com/problems/sum-root-to-leaf-numbers/
 **/
public class Solution {
    public int sumNumbers(TreeNode root) {
        return sumHelper(root, 0);
    }

    public int sumHelper(TreeNode root, int sum) {
        if (root == null) {
            // left + right
            return 0;
        }

        // root
        // leaf node
        if (root.left == null && root.right == null) {
            return 10 * sum + root.val;
        }

        // left and right
        return sumHelper(root.left, 10 * sum + root.val) + sumHelper(root.right, 10 * sum + root.val);
    }
}
