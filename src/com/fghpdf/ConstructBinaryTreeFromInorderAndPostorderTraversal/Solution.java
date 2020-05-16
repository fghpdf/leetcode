package com.fghpdf.ConstructBinaryTreeFromInorderAndPostorderTraversal;

import java.util.HashMap;
import java.util.Map;

/**
 * @author fghpdf
 * @date 2020/5/16
 * @link https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
 * postOrder need from right -> left
 **/
public class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        Map<Integer, Integer> inOrderIndexMap = new HashMap<>(inorder.length);
        for (int i = 0; i < inorder.length; i++) {
            inOrderIndexMap.put(inorder[i], i);
        }

        return builder(0, inorder.length - 1, postorder, 0, postorder.length - 1, inOrderIndexMap);
    }

    private TreeNode builder(int inStart, int inEnd, int[] postorder, int postStart, int postEnd, Map<Integer, Integer> inOrderIndexMap) {
        if (inStart > inEnd || postStart > postEnd) {
            return null;
        }

        // root
        TreeNode root = new TreeNode(postorder[postEnd]);

        int inRootIndex = inOrderIndexMap.get(root.val);
        int rightSubTreeNums = inEnd - inRootIndex;

        // right
        root.right = builder(inRootIndex + 1, inEnd, postorder, postEnd - rightSubTreeNums, postEnd - 1, inOrderIndexMap);
        // left
        root.left = builder(inStart, inRootIndex - 1, postorder, postStart, postEnd - rightSubTreeNums - 1, inOrderIndexMap);
        return root;
    }
}
