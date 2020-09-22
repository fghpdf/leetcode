package com.fghpdf.BinaryTreePreorderTraversal;

import com.fghpdf.TreeNode;

import java.util.ArrayList;
import java.util.List;

/**
 * @author qxx
 * @date 9/22/2020
 * @link https://leetcode.com/problems/binary-tree-preorder-traversal/
 **/
public class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) {
            return result;
        }

        // preorder
        // root
        result.add(root.val);

        // left
        result.addAll(preorderTraversal(root.left));

        // right
        result.addAll(preorderTraversal(root.right));

        return result;
    }
}
