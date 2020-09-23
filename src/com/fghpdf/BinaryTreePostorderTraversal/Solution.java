package com.fghpdf.BinaryTreePostorderTraversal;

import com.fghpdf.TreeNode;

import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

/**
 * @author qxx
 * @date 9/23/2020
 * @link https://leetcode.com/problems/binary-tree-postorder-traversal/
 **/
public class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new LinkedList<>();
        if (root == null) {
            return result;
        }
        // postorder

        // left
        result.addAll(postorderTraversal(root.left));
        // right
        result.addAll(postorderTraversal(root.right));
        // root
        result.add(root.val);

        return result;
    }

    public List<Integer> iterative(TreeNode root) {
        List<Integer> result = new LinkedList<>();
        if (root == null) {
            return result;
        }

        Stack<TreeNode> nodeStack = new Stack<>();
        nodeStack.push(root);

        while (!nodeStack.isEmpty()) {
            TreeNode current = nodeStack.pop();
            result.add(0, current.val);

            if (current.left != null) {
                nodeStack.push(current.left);
            }

            if (current.right != null) {
                nodeStack.push(current.right);
            }
        }

        return result;
    }
}
