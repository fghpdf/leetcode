package com.fghpdf.CoinChange2;

/**
 * @author fghpdf
 * @date 2020/5/25
 * @link https://leetcode.com/problems/coin-change-2/
 **/
public class Solution {
    public int change(int amount, int[] coins) {
        int[][] dp = new int[coins.length + 1][amount + 1];

        // base
        for (int i = 0; i < amount + 1; i++) {
            dp[0][i] = 0;
        }
        for (int i = 0; i < coins.length + 1; i++) {
            dp[i][0] = 1;
        }

        // loop [1, coins]
        for (int i = 1; i < coins.length + 1; i++) {
            // loop [1, amount]
            for (int j = 1; j < amount + 1; j++) {
                // choose
                if (j - coins[i-1] >= 0) {
                    dp[i][j] = dp[i-1][j] +
                            dp[i][j-coins[i-1]];
                } else {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }

        return dp[coins.length][amount];
    }
}
