package com.fghpdf.MergeSortedArray;

/**
 * https://leetcode.com/problems/merge-sorted-array/
 * @author fghpdf
 * the problem needs to use nums1 to get result
 * so we can get every biggest number and place it to tail.
 */
public class Solution {
	public void merge(int[] nums1, int m, int[] nums2, int n) {
		int tail1 = m - 1;
		int tail2 = n - 1;
		int tailResult = m + n - 1;

		while (tail1 >= 0 && tail2 >= 0) {
			nums1[tailResult] = nums1[tail1] > nums2[tail2] ?
					nums1[tail1--] : nums2[tail2--];
			tailResult--;
		}

		while (tail2 >= 0) {
			nums1[tailResult] = nums2[tail2];
			tailResult--;
			tail2--;
		}
	}
}
