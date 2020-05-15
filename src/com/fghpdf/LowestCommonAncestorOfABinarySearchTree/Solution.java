package com.fghpdf.LowestCommonAncestorOfABinarySearchTree;

/**
 * @author fghpdf
 * @date 2020/5/15
 * @link https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
 * due to BST, so can sure LCA position
 **/
public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // a node to be a descendant of itsel
        if ((root.val - p.val) * (root.val - q.val) < 1) {
            return root;
        }

        // must be left or right
        if (p.val < root.val) {
            //left
            return lowestCommonAncestor(root.left, p, q);
        }

        // right
        return lowestCommonAncestor(root.right, p, q);
    }
}
