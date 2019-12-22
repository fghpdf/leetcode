package com.fghpdf.PerfectSquares;

import java.util.Arrays;

/**
 * @author fghpdf
 * @date 2019/12/22
 * https://leetcode.com/problems/perfect-squares/
 * dp[0] = 0
 * dp[1] = dp[0]+1 = 1
 * dp[2] = dp[1]+1 = 2
 * dp[3] = dp[2]+1 = 3
 * dp[4] = Min{ dp[4-1*1]+1, dp[4-2*2]+1 }
 *       = Min{ dp[3]+1, dp[0]+1 }
 *       = 1
 * dp[n] = Min{ dp[n - i*i] + 1 },  n - i*i >=0 && i >= 1
 **/
public class Solution {
	public int numSquares(int n) {
		int[] dp = new int[n + 1];
		Arrays.fill(dp, Integer.MAX_VALUE);
		dp[0] = 0;
		for (int i = 1; i <= n; i++) {
			int min = Integer.MAX_VALUE;
			int j = 1;
			while (i - j * j >= 0) {
				min = Math.min(min, dp[i - j * j] + 1);
				j++;
			}
			dp[i] = min;
		}
		return dp[n];
	}

	public static void main(String[] args) {
		Solution solution = new Solution();
		System.out.println(solution.numSquares(12));
	}
}
