package com.fghpdf.BinarySearchTreeIterator;

import com.fghpdf.TreeNode;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * @author qxx
 * @date 9/24/2020
 * @link https://leetcode.com/problems/binary-search-tree-iterator/
 **/
public class Solution {
    Queue<Integer> sorted = new LinkedList<>();

    public void BSTIterator(TreeNode root) {
        this.sorted = sortTree(root);
    }

    private Queue<Integer> sortTree(TreeNode root) {
        Queue<Integer> result = new LinkedList<>();
        if (root == null) {
            return result;
        }

        // inorder
        // left
        result.addAll(sortTree(root.left));
        // root
        result.add(root.val);
        // right
        result.addAll(sortTree(root.right));

        return result;
    }

    /** @return the next smallest number */
    public int next() {
        return this.sorted.poll();
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !this.sorted.isEmpty();
    }
}
