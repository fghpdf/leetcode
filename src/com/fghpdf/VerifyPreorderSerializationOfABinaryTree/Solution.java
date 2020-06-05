package com.fghpdf.VerifyPreorderSerializationOfABinaryTree;

/**
 * @author fghpdf
 * @date 2020/6/5
 * @link https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
 **/
public class Solution {
    public boolean isValidSerialization(String preorder) {
        String[] nodes = preorder.split(",");
        return helper(nodes, 0) == nodes.length - 1;
    }

    private int helper(String[] nodes, int current) {
        if (current >= nodes.length) {
            return -1;
        }

        // leaf node
        if ("#".equals(nodes[current])) {
            return current;
        }

        // left
        int next = helper(nodes, current + 1);
        if (next == -1) {
            return -1;
        }

        // right
        next = helper(nodes, next + 1);

        return next;
    }
}
