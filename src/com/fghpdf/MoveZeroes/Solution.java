package com.fghpdf.MoveZeroes;

/**
 * @author fghpdf
 * @date 2019/11/6
 *
 * https://leetcode.com/problems/move-zeroes/
 * loop nums to get non-zero number and insert looped position
 * and then set zero from the last position.
 **/
public class Solution {
	public void moveZeroes(int[] nums) {
		if (nums.length == 0) {
			return;
		}

		int position = 0;
		for (int num : nums) {
			System.out.println(num);
			if (num != 0) {
				nums[position++] = num;
			}
		}

		for (int i = position; i < nums.length; i++) {
			nums[i] = 0;
		}
	}

	public static void main(String[] args) {
		Solution sol = new Solution();
		int[] nums = {1,0,3};

		sol.moveZeroes(nums);
	}
}
