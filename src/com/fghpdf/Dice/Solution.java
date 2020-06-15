package com.fghpdf.Dice;

/**
 * @author fghpdf
 * @date 2020/6/15
 * @link https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/
 **/
public class Solution {
    public double[] twoSum(int n) {
        // The nth dice 's number s times
        int[][] dp = new int[n + 1][6*n + 1];
        
        // init
        // 1 dice 's number will appear 1 times
        for (int i = 1; i <= 6; i++) {
            dp[1][i] = 1;
        }

        // loop dice
        for (int dice = 2; dice <= n; dice++) {
            // loop all dices number sum
            for (int sum = dice; sum <= 6 * dice; sum++) {
                // loop times
                for (int times = 1; times <= 6; times++) {
                    if (sum - times < dice - 1) {
                        break;
                    }
                    dp[dice][sum] += dp[dice-1][sum - times];
                }
            }
        }

        // Probability
        double total = Math.pow((double) 6, (double) n);
        double[] result = new double[5*n + 1];
        for (int i = n; i <= 6*n; i++) {
            result[i-n] = ((double) dp[n][i]) / total;
        }

        return result;
    }
}
