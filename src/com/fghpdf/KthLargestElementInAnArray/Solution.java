package com.fghpdf.KthLargestElementInAnArray;

import java.util.Arrays;
import java.util.Comparator;

/**
 * @author fghpdf
 * @date 2019/12/17
 * https://leetcode.com/problems/kth-largest-element-in-an-array/
 *
 * sort ...
 **/
public class Solution {
	public int findKthLargest(int[] nums, int k) {
		int[] sorted = Arrays.stream(nums).boxed()
				.sorted(Comparator.reverseOrder())
				.mapToInt(Integer::intValue)
				.toArray();

		return sorted[k - 1];
	}
}
