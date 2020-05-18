package com.fghpdf.MaximalSquare;

/**
 * @author fghpdf
 * @date 2020/5/18
 * @link https://leetcode.com/problems/maximal-square/
 **/
public class Solution {
    public int maximalSquare(char[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }

        int max = 0;

        // dp[i, j] is the lower right maximal square's length
        // dp[i, j] is min{dp[i-1, j], dp[i-1,j-1], dp[i,j-1]} + 1
        // because the length depends on the min square's length
        int[][] dp = new int[matrix.length + 1][matrix[0].length + 1];

        // loop input
        for (int row = 1;row <= matrix.length; row++) {
            for (int col = 1; col <= matrix[0].length; col++) {
                // should be last element
                if (matrix[row - 1][col - 1] == '1') {
                    dp[row][col] = Math.min(Math.min(dp[row-1][col], dp[row-1][col-1]), dp[row][col-1]) + 1;
                    max = Math.max(max, dp[row][col]);
                }
            }
        }

        return max * max;

    }
}
