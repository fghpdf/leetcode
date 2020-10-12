package com.fghpdf.BinaryTreeRightSideView;

import com.fghpdf.PopulatingNextRightPointersInEachNodeII.Node;
import com.fghpdf.TreeNode;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * @author qxx
 * @date 10/12/2020
 * @link https://leetcode.com/problems/binary-tree-right-side-view/
 **/
public class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new LinkedList<>();
        if (root == null) {
            return result;
        }

        // level
        Queue<TreeNode> levelNodes = new LinkedList<>();

        // init
        levelNodes.offer(root);

        while (!levelNodes.isEmpty()) {
            // memo this level node number
            int thisLevelNodesNum = levelNodes.size();
            // from left to right to find the node can be seen
            TreeNode canBeSeenNode = null;
            for (int i = 0; i < thisLevelNodesNum; i++) {
                // add next level nodes to queue
                TreeNode thisNode = levelNodes.peek();
                if (thisNode == null) {
                    continue;
                }

                if (thisNode.left != null) {
                    levelNodes.offer(thisNode.left);
                }

                if (thisNode.right != null) {
                    levelNodes.offer(thisNode.right);
                }

                canBeSeenNode = thisNode;
                levelNodes.poll();
            }

            if (canBeSeenNode == null) {
                // over
                return result;
            }

            result.add(canBeSeenNode.val);
        }

        return result;
    }
}
