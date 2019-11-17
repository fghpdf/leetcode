package com.fghpdf.FindFirstAndLastPositionOfElementInSortedArray;

import java.util.Arrays;

/**
 * @author fghpdf
 * @date 2019/11/17
 * https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
 * left side and right side also use binary search
 **/
public class Solution {
	public int[] searchRange(int[] nums, int target) {
		int low = 0;
		int high = nums.length - 1;
		int first = -1;
		int last = -1;

		while (low <= high) {
			int mid = (low + high) / 2;
			if (nums[mid] == target) {
				first = findFirstPosition(Arrays.copyOfRange(nums, 0, mid + 1), target);
				last = mid + findLastPosition(Arrays.copyOfRange(nums, mid, nums.length), target);
				return new int[]{first, last};
			}

			if (nums[mid] < target) {
				low = mid + 1;
			} else {
				high = mid - 1;
			}
		}

		return new int[]{first, last};
	}

	private int findFirstPosition(int[] nums, int target) {
		int low = 0;
		int high = nums.length - 1;

		while (low <= high) {
			int mid = (low + high) / 2;
			if (nums[mid] == target && (mid == 0 || nums[mid - 1] != target)) {
				return mid;
			}
			if (nums[mid] < target) {
				low = mid + 1;
			} else {
				high = mid - 1;
			}
		}

		return -1;
	}

	private int findLastPosition(int[] nums, int target) {
		int low = 0;
		int high = nums.length - 1;

		while (low <= high) {
			int mid = (low + high) / 2;
			if (nums[mid] == target && (mid == nums.length - 1 || nums[mid + 1] != target)) {
				return mid;
			}
			if (nums[mid] <= target) {
				low = mid + 1;
			} else {
				high = mid - 1;
			}
		}
		return -1;
	}

	public static void main(String[] args) {
		Solution solution = new Solution();
		System.out.println(Arrays.toString(solution.searchRange(new int[]{5, 7, 7, 8,8, 8, 10}, 8)));
	}
}
