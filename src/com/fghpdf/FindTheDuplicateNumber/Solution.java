package com.fghpdf.FindTheDuplicateNumber;

/**
 * @author fghpdf
 * @date 2019/12/23
 * https://leetcode.com/problems/find-the-duplicate-number/
 * fast and slow
 * When fast==slow, they meet at the entry point of the circle
 **/
public class Solution {
	public int findDuplicate3(int[] nums) {
		if (nums.length < 1) {
			return -1;
		}

		int slow = nums[0];
		int fast = nums[slow];
		while (slow != fast) {
			slow = nums[slow];
			fast = nums[nums[fast]];
		}

		fast = 0;
		while (slow != fast) {
			fast = nums[fast];
			slow = nums[slow];
		}

		return slow;
	}
}
