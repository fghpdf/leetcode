package com.fghpdf.PartitionEqualSubsetSum;

import java.util.Arrays;

/**
 * @author fghpdf
 * @date 2020/5/21
 * @link https://leetcode.com/problems/partition-equal-subset-sum/
 * status is { capacity: sum/2, nums }
 * chose is { put in or not}
 * dp[i][j] is that No.i-1 items sum can equal j in two ways
 * base case dp[0][...] is false beacuse no items can put
 * dp[...][0] is true because no capacity needs items to put in
 **/
public class Solution {
    public boolean canPartition(int[] nums) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        // odd sum will never get two part can equal
        if (sum % 2 != 0) {
            return false;
        }

        // init
        // dp[i][j] is that No.i-1 items sum can equal j in two ways
        // put in or not
        boolean[][] dp = new boolean[nums.length+1][sum/2+1];
        // no items
        Arrays.fill(dp[0], false);
        // no capacity
        for (int i = 0; i <= nums.length; i++) {
            dp[i][0] = true;
        }

        // loop [1, nums.length]
        for (int i = 1; i <= nums.length; i++) {
            for (int j = 0; j <= sum / 2; j++) {
                // can't put in cause no enough value
                if (j - nums[i - 1] > 0 ) {
                    dp[i][j] = dp[i-1][j];
                } else {
                    // put in or not
                    dp[i][j] = dp[i-1][j] || dp[i-1][j - nums[i-1]];
                }
            }
        }

        return dp[nums.length][sum/2];
    }
}
