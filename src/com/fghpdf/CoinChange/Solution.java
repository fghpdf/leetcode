package com.fghpdf.CoinChange;

/**
 * @author fghpdf
 * @date 2019/12/29
 * https://leetcode.com/problems/coin-change/
 * dp coins [1,2,5] amount 11
 * dp[0] is 0
 * dp[1] is 1. coin 1
 * dp[2] is 1. coin 2. min(coin 2 + dp[0]...coin 1 + dp[1])
 * ...
 * dp[11] is 3. min(coin 5 + dp[6]...coin 3 + dp[8]...coin 1 + dp[10])
 **/
public class Solution {
	public int coinChange(int[] coins, int amount) {
		if (amount < 1) {
			return amount;
		}
		return helper(coins, amount, new int[amount]);
	}

	private int helper(int[] coins, int rem, int[] dp) {
		if (rem < 0) {
			return -1;
		}

		if (rem == 0) {
			return 0;
		}

		if (dp[rem - 1] != 0) {
			return dp[rem - 1];
		}

		int min = Integer.MAX_VALUE;
		for (int coin : coins) {
			int res = helper(coins, rem - coin, dp);
			if (res >= 0 && res < min) {
				min = res + 1;
			}
		}
		dp[rem - 1] = (min == Integer.MAX_VALUE) ? -1 : min;
		return dp[rem - 1];
	}

	public static void main(String[] args) {
		Solution solution = new Solution();
		System.out.println(solution.coinChange(new int[]{1, 2, 5}, 11));
	}
}
