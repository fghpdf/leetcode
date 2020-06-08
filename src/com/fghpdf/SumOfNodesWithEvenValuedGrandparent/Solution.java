package com.fghpdf.SumOfNodesWithEvenValuedGrandparent;

import com.fghpdf.TreeNode;

/**
 * @author fghpdf
 * @date 2020/6/8
 * @link https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
 **/
public class Solution {

    public int sumEvenGrandparent(TreeNode root) {
        return helper(root);
    }

    private int helper(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int sum = 0;
        // exit
        // isEven
        if (root.val % 2 == 0) {
            if (root.left != null && root.left.left != null) {
                sum += root.left.left.val;
            }

            if (root.left != null && root.left.right != null) {
                sum += root.left.right.val;
            }

            if (root.right != null && root.right.left != null) {
                sum += root.right.left.val;
            }

            if (root.right != null && root.right.right != null) {
                sum += root.right.right.val;
            }
        }

        // left
        int left = helper(root.left);
        // right
        int right = helper(root.right);

        return sum + left + right;
    }
}
