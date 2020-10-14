package com.fghpdf.BinaryTreePaths;

import com.fghpdf.TreeNode;

import java.util.LinkedList;
import java.util.List;

/**
 * @author qxx
 * @date 10/14/2020
 * @link https://leetcode.com/problems/binary-tree-paths/
 **/
public class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> result = new LinkedList<>();
        findPath(root, "", result);
        return result;
    }

    private void findPath(TreeNode root, String path, List<String> result) {
        if (root == null) {
            return;
        }

        if (path.equals("")) {
            path = path + root.val;
        } else {
            path = path + "->" + root.val;
        }

        if (root.left == null && root.right == null) {
            result.add(path);
            return;
        }

        findPath(root.left, path, result);
        findPath(root.right, path, result);
    }
}
