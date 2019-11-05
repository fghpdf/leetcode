package com.fghpdf.MissingNumber;

import java.util.Arrays;

/**
 * @author fghpdf
 * @date 2019/11/5
 *
 * https://leetcode.com/problems/missing-number/
 * the best way is use XOR, XOR can get
 * result = result ^ b ^ b
 *
 * so we can judge nums[i] and i is same number
 **/
public class Solution {
	public int missingNumber(int[] nums) {
		boolean[] isContain = new boolean[nums.length + 1];
		Arrays.fill(isContain, false);

		for (int num : nums) {
			isContain[num] = true;
		}

		for (int i = 0; i < isContain.length; i++) {
			if (!isContain[i]) {
				return i;
			}
		}

		return 0;
	}

	public int anthoer(int[] nums) {
		int result = nums.length;
		for (int i = 0; i < nums.length; i++) {
			result = result ^ i ^ nums[i];
		}

		return result;
	}

	public static void main(String[] args) {
		Solution sol = new Solution();
		int[] nums  = {3,0,1};

		System.out.println(sol.anthoer(nums));
	}
}
