package com.fghpdf.HouseRobberIII;

import com.fghpdf.TreeNode;

/**
 * @author qxx
 * @date 10/14/2020
 * @link https://leetcode.com/problems/house-robber-iii/
 **/
public class Solution {
    public int rob(TreeNode root) {
        int[] res = robSub(root);
        return Math.max(res[0], res[1]);
    }

    private int[] robSub(TreeNode root) {
        if (root == null) {
            return new int[2];
        }

        int[] left = robSub(root.left);
        int[] right = robSub(root.right);
        int[] res = new int[2];

        // the sub tree level
        res[0] = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        // root + sub sub tree
        res[1] = root.val + left[0] + right[0];

        return res;
    }
}
