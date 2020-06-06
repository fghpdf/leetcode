package com.fghpdf.SerializeAndDeserializeBinaryTree;

import com.fghpdf.TreeNode;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

/**
 * @author fghpdf
 * @date 2020/6/6
 * @link https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
 **/
public class Solution {

    private final String SPLITER = ",";
    private final String NULLNODE = "#";

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        // pre order
        serializeHelper(root, sb);
        return sb.toString();
    }

    private void serializeHelper(TreeNode root, StringBuilder stringBuilder) {
        // null is #
        if (root == null) {
            stringBuilder.append(NULLNODE).append(SPLITER);
            return;
        }

        stringBuilder.append(root.val).append(SPLITER);
        // left
        serializeHelper(root.left, stringBuilder);
        // right
        serializeHelper(root.right, stringBuilder);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        Queue<String> nodes = new LinkedList<>(Arrays.asList(data.split(SPLITER)));
        return deserializeHelper(nodes);
    }

    private TreeNode deserializeHelper(Queue<String> nodes) {
        String nodeValue = nodes.remove();
        // # is null
        if (NULLNODE.equals(nodeValue)) {
            return null;
        }

        TreeNode root = new TreeNode(Integer.parseInt(nodeValue));

        // left
        root.left = deserializeHelper(nodes);
        // right
        root.right = deserializeHelper(nodes);

        return root;
    }
}
