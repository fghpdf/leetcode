package com.fghpdf.ClimbingStairs;

/**
 * https://leetcode.com/problems/climbing-stairs/
 * dynamic programming problem
 * you should to calc 3 4 5 and so on result
 * and then the final result is n-1 add n-2
 * @author fghpdf
 */
public class Solution {
	public int climbStairs(int n) {
		int[] dp = new int[n + 1];
		if (n == 2) {
			return 2;
		}

		if (n == 1) {
			return 1;
		}

		if (n <= 0) {
			return 0;
		}
		dp[0] = 0;
		dp[1] = 1;
		dp[2] = 2;

		for (int i = 3; i <= n;i++) {
			dp[i] = dp[i-1] + dp[i-2];
		}

		return dp[n];
	}

	public static void main(String[] args) {
		Solution sol = new Solution();
		System.out.println(sol.climbStairs(44));
	}
}
