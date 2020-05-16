package com.fghpdf.UniqueBinarySearchTrees;

/**
 * @author fghpdf
 * @date 2020/5/16
 * @link https://leetcode.com/problems/unique-binary-search-trees/
 * actually dp[n] is result, we assume a root i
 * left is dp[i-1](no root), right is dp[n-i]
 * they shoubld dp[n] = dp[i-1] * dp[n-i]
 **/
public class Solution {
    public int numTrees(int n) {
        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = 1;

        // loop [2, n]
        for (int i = 2; i <= n; i++) {
            // loop [1, i]
            for (int j = 1; j <= i; j++) {
                // left * right
                // j is root
                dp[i] += dp[j - 1] * dp[i - j];
            }
        }

        return dp[n];
    }
}
