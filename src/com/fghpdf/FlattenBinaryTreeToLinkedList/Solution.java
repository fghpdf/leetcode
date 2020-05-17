package com.fghpdf.FlattenBinaryTreeToLinkedList;

import java.util.LinkedList;
import java.util.Queue;

/**
 * @author fghpdf
 * @date 2020/5/17
 * @link https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
 * this case use inorder so can simulation it
 * then get inorder queue and insert right subtree
 **/
public class Solution {
    public void flatten(TreeNode root) {
        if (root == null) {
            return;
        }
        Queue<TreeNode> tempInorder = new LinkedList<>();
        traverse(root, tempInorder);
        // init root
        tempInorder.poll();
        root.left = null;

        // load right subtree
        while(!tempInorder.isEmpty()) {
            root.right = tempInorder.poll();
            root = root.right;
        }
    }

    private void traverse(TreeNode root, Queue<TreeNode> tempInorder) {
        if (root == null) {
            return;
        }
        // root
        tempInorder.offer(new TreeNode(root.val));
        // left
        traverse(root.left, tempInorder);
        // right
        traverse(root.right, tempInorder);
    }
}
