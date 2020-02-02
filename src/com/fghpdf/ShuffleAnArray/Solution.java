package com.fghpdf.ShuffleAnArray;

import java.util.Random;

/**
 * @author fghpdf
 * @date 2020/2/2
 * @link https://leetcode.com/problems/shuffle-an-array/
 *
 **/
public class Solution {

	private int[] nums;
	private Random random;

	public Solution(int[] nums) {
		this.nums = nums;
		random = new Random();
	}

	/** Resets the array to its original configuration and return it. */
	public int[] reset() {
		return nums;
	}

	/** Returns a random shuffling of the array. */
	public int[] shuffle() {
		int[] randomNums = new int[nums.length];
		for (int i = 0; i < nums.length; i++) {
			int position = random.nextInt(i + 1);
			randomNums[i] = randomNums[position];
			randomNums[position] = nums[i];
		}

		return randomNums;
	}
}
