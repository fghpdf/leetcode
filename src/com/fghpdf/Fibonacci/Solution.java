package com.fghpdf.Fibonacci;

/**
 * @author fghpdf
 * @date 2020/6/8
 * @link https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/
 **/
public class Solution {
    public int fib(int n) {
        if (n == 0) {
            return 0;
        }

        int[] dp = new int[n+1];
        dp[1] = 1;
        dp[0] = 0;

        for (int i = 3; i < n + 1; i++) {
            dp[i] = dp[i-1] + dp[i-2];
            // big number
            dp[i] %= 1000000007;
        }

        return dp[n];
    }
}
