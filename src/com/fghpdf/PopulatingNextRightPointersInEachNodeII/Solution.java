package com.fghpdf.PopulatingNextRightPointersInEachNodeII;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * @author fghpdf
 * @date 2020/5/17
 * @link https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
 * use BinaryTreeLevelOrderTraversal template to loop level
 * and then get row nodes and connected
 **/
public class Solution {
    public Node connect(Node root) {
        if (root == null) {
            return root;
        }

        // loop level
        Queue<Node> levelNodes = new LinkedList<>();

        // init
        levelNodes.offer(root);

        while(!levelNodes.isEmpty()) {
            int thisLevelNodesNums = levelNodes.size();
            List<Node> row = new LinkedList<>();
            for (int i = 0; i < thisLevelNodesNums; i++) {
                Node thisLevelNode = levelNodes.peek();
                if (thisLevelNode == null) {
                    continue;
                }

                if (thisLevelNode.left != null) {
                    levelNodes.offer(thisLevelNode.left);
                }

                if (thisLevelNode.right != null) {
                    levelNodes.offer(thisLevelNode.right);
                }

                row.add(thisLevelNode);
                levelNodes.poll();
            }

            if (row.size() <= 1) {
                continue;
            }

            // connect
            Node prev = row.get(0);
            for (int i = 1; i < row.size(); i++ ) {
                prev.next = row.get(i);
                prev = row.get(i);
            }
        }

        return root;

    }

}
