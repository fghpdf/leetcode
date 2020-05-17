package com.fghpdf.PathSumII;

import java.util.LinkedList;
import java.util.List;

/**
 * @author fghpdf
 * @date 2020/5/17
 * @link https://leetcode.com/problems/path-sum-ii/submissions/
 * actually is backtrack item
 * end condition is sum - root.val == 0
 * choose is {left, right}
 * remeber remove temp last element
 **/
public class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> result = new LinkedList<>();
        backtrackPathSum(root, new LinkedList<>(), sum, result);
        return result;
    }

    private void backtrackPathSum(TreeNode root, List<Integer> tempList, int remainingSum, List<List<Integer>> result) {
        if (root == null) {
            return;
        }

        // end condition
        if (remainingSum == root.val) {
            // leaf node
            if (root.left == null && root.right == null) {
                // extra step
                tempList.add(root.val);
                result.add(new LinkedList<>(tempList));
                tempList.remove(tempList.size() - 1);
            }
        }

        // choose
        // left
        tempList.add(root.val);
        backtrackPathSum(root.left, tempList, remainingSum - root.val, result);
        // un choose
        tempList.remove(tempList.size() - 1);

        // choose
        // right
        tempList.add(root.val);
        backtrackPathSum(root.right, tempList, remainingSum - root.val, result);
        // un choose
        tempList.remove(tempList.size() - 1);
    }
}
