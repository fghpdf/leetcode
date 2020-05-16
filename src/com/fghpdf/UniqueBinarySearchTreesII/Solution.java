package com.fghpdf.UniqueBinarySearchTreesII;

import java.util.LinkedList;
import java.util.List;

/**
 * @author fghpdf
 * @date 2020/5/16
 * @link https://leetcode.com/problems/unique-binary-search-trees-ii/
 * Still like tree template
 * Recursive to get left and right tree
 * then add to the root
 * but this case should loop left -> right to genrate root tree
 **/
public class Solution {
    public List<TreeNode> generateTrees(int n) {
        if (n == 0) {
            return new LinkedList<>();
        }
        return genFromRange(1, n);
    }

    private List<TreeNode> genFromRange(int start, int end) {
        List<TreeNode> result = new LinkedList<>();
        // exit
        if (start > end) {
            result.add(null);
            return result;
        }

        // loop [start, end]
        for (int i = start; i <= end; i++) {
            // left
            List<TreeNode> leftNodes = genFromRange(start, i - 1);
            // right
            List<TreeNode> rightNodes = genFromRange(i + 1, end);
            for (TreeNode leftNode : leftNodes) {
                for (TreeNode rightNode : rightNodes) {
                    TreeNode root = new TreeNode(i);
                    root.left = leftNode;
                    root.right = rightNode;
                    result.add(root);
                }
            }
        }

        return result;
    }
}
