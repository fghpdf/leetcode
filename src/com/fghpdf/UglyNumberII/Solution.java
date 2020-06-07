package com.fghpdf.UglyNumberII;

/**
 * @author fghpdf
 * @date 2020/6/7
 * @link https://leetcode.com/problems/ugly-number-ii/
 **/
public class Solution {
    public int nthUglyNumber(int n) {
        // 2 3 5
        int i = 0, j = 0, k = 0;
        int p = 1;

        int[] dp = new int[n];
        dp[0] = 1;

        while (p < n) {
            dp[p] = Math.min(2 * dp[i], Math.min(3 * dp[j], 5 * dp[k]));
            if (dp[p] == 2 * dp[i]) {
                i++;
            }

            if (dp[p] == 3 * dp[j]) {
                j++;
            }

            if (dp[p] == 5 * dp[k]) {
                k++;
            }

            p++;
        }

        return dp[n-1];
    }
}
