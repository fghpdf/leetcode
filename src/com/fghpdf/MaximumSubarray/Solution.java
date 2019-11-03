package com.fghpdf.MaximumSubarray;

/**
 * sum(0,i) = a[i] + (sum(0,i-1) < 0 ? 0 : sum(0,i-1))
 * https://leetcode.com/problems/maximum-subarray/
 */


public class Solution {
	public int maxSubArray(int[] nums) {
		if (nums == null || nums.length == 0) { return 0; }
		int max = nums[0], sum = nums[0];
		for (int i = 1; i < nums.length; i++) {
			if (sum < 0) {
				sum = nums[i];
			} else {
				sum += nums[i];
			}

			max = Math.max(max, sum);
		}
		return max;
	}
}
