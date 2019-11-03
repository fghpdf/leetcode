package com.fghpdf.RotateArray;

/**
 * @author fghpdf
 * @date 2019/10/26
 *
 * https://leetcode.com/problems/rotate-array/
 * nums = "----->-->"; k =3
 * result = "-->----->";
 *
 * reverse "----->-->" we can get "<--<-----"
 * reverse "<--" we can get "--><-----"
 * reverse "<-----" we can get "-->----->"
 **/
public class Solution {
	public void rotate(int[] nums, int k) {
		k %= nums.length;

		reverse(nums, 0, nums.length - 1);
		reverse(nums, 0, k - 1);
		reverse(nums, k, nums.length - 1);
	}

	private void reverse(int[] nums, int start, int end) {
		while (start < end) {
			int temp = nums[start];
			nums[start] = nums[end];
			nums[end] = temp;
			start++;
			end--;
		}
	}
}
