package com.fghpdf.SingleNumber;

/**
 * https://leetcode.com/problems/single-number/
 * @author fghpdf
 *
 * I learned XOR operator, awesome
 * the array is {2,1,4,5,2,4,1}
 * 2 ^ 1 ^ 4 ^ 5 ^ 2 ^ 4 ^ 1 =>
 * (2 ^ 2) ^ (1 ^ 1) ^ (4 ^ 4) ^ 5 =>
 * (0^0^0^0^5) => 5
 */
public class Solution {
	public int singleNumber(int[] nums) {
		for (int i = 1; i < nums.length; i++) {
			nums[0] ^= nums[i];
		}
		return nums[0];
	}
}
