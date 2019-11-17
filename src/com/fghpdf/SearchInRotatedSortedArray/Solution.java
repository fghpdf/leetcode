package com.fghpdf.SearchInRotatedSortedArray;

/**
 * @author fghpdf
 * @date 2019/11/17
 * https://leetcode.com/problems/search-in-rotated-sorted-array/
 *
 * binary search
 * but we must find the smallest point, and then to binary search
 **/
public class Solution {
	public int search(int[] nums, int target) {
		int root = findRootPosition(nums);
		int low = 0;
		int high = nums.length - 1;
		while (low <= high) {
			int mid = (low + high) / 2;
			// i don't why, remember it
			int realMid = (mid + root) % nums.length;
			if (nums[realMid] == target) {
				return realMid;
			}
			// binary search, lower is in left, higher is in right
			if (nums[realMid] < target) {
				low = mid + 1;
			} else {
				high = mid - 1;
			}
		}
		return -1;
	}

	private int findRootPosition(int[] nums) {
		int low = 0;
		int high = nums.length - 1;

		while (low < high) {
			int mid = (low + high) / 2;
			// mid > high: the root(smallest) is in right
			if (nums[mid] > nums[high]) {
				low = mid + 1;
			} else {
				high = mid;
			}
		}

		return low;
	}
}
