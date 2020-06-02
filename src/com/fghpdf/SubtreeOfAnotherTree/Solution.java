package com.fghpdf.SubtreeOfAnotherTree;

import com.fghpdf.TreeNode;

/**
 * @author fghpdf
 * @date 2020/6/2
 * @link https://leetcode.com/problems/subtree-of-another-tree/
 **/
public class Solution {
    public boolean isSubtree(TreeNode s, TreeNode t) {
        if (s == null) {
            return false;
        }

        // root
        if (isSame(s, t)) {
            return true;
        }

        // left or right
        return isSubtree(s.left, t) || isSubtree(s.right, t);
    }

    private boolean isSame(TreeNode s, TreeNode t) {
        if (s == null || t == null) {
            return s == t;
        }

        if (s.val != t.val) {
            return false;
        }

        // depth compare s and t
        return isSame(s.left, t.left) && isSame(s.right, t.right);
    }
}
