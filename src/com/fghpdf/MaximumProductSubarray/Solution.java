package com.fghpdf.MaximumProductSubarray;

/**
 * @author fghpdf
 * @date 2019/12/10
 * https://leetcode.com/problems/maximum-product-subarray/
 * dp can save two status max and min
 * dp[i] = max dp[i-1].max * number, dp[i-1].min * number
 **/
public class Solution {
	public int maxProduct(int[] nums) {
		Tuple[] dp = new Tuple[nums.length];
		dp[0] = new Tuple(nums[0], nums[0]);
		int res = dp[0].iMax;
		for (int i = 1; i < nums.length; i++) {
			Tuple prev = dp[i - 1];
			int iMax = Math.max(Math.max(nums[i], nums[i] * prev.iMax), nums[i] * prev.iMin);
			int iMin = Math.min(Math.min(nums[i], nums[i] * prev.iMax), nums[i] * prev.iMin);
			dp[i] = new Tuple(iMax, iMin);
			res = Math.max(iMax, res);
		}
		return res;
	}

	class Tuple {
		private int iMax;
		private int iMin;
		private Tuple(int iMax, int iMin) {
			this.iMax = iMax;
			this.iMin = iMin;
		}
	}
}
