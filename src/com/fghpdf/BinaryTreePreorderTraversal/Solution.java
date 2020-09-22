package com.fghpdf.BinaryTreePreorderTraversal;

import com.fghpdf.TreeNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

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

    public List<Integer> iterative(TreeNode root) {
        List<Integer> result = new LinkedList<>();
        if (root == null) {
            return result;
        }

        // stock right node
        Stack<TreeNode> rightNodes = new Stack<>();

        // loop
        while (root != null) {
            result.add(root.val);
            if (root.right != null) {
                rightNodes.add(root.right);
            }

            root = root.left;

            // leaf
            if (root == null && !rightNodes.isEmpty()) {
                root = rightNodes.pop();
            }
        }

        return result;
    }
}
