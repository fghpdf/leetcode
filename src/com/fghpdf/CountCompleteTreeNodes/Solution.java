package com.fghpdf.CountCompleteTreeNodes;

import com.fghpdf.TreeNode;

/**
 * @author qxx
 * @date 10/13/2020
 * @link https://leetcode.com/problems/count-complete-tree-nodes/
 **/
public class Solution {
    public int countNodes(TreeNode root) {
        int leftDepth = getLeftDepth(root);
        int rightDepth = getRightDepth(root);

        if (leftDepth == rightDepth) {
            // full binary tree nodes is 2^depth - 1
            return (1 << leftDepth) - 1;
        } else {
            return 1 + countNodes(root.left) + countNodes(root.right);
        }
    }

    private int getRightDepth(TreeNode root) {
        int depth = 0;
        while (root != null) {
            depth++;
            root = root.right;
        }

        return depth;
    }

    private int getLeftDepth(TreeNode root) {
        int depth = 0;
        while (root != null) {
            depth++;
            root = root.left;
        }

        return depth;
    }
}
