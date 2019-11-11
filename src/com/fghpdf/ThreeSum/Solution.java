package com.fghpdf.ThreeSum;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @author fghpdf
 * @date 2019/11/11
 * https://leetcode.com/problems/3sum/
 *
 * can't to loop 3 times, it will overtime
 * first sort
 * then loop 1 time and to compute 3 numbers
 * if sum == 0, should eliminate same numbers
 * if sum < 0, lower number is too small
 * if sum > 0, higher number is too big
 **/
public class Solution {
	public List<List<Integer>> threeSum(int[] nums) {
		Arrays.sort(nums);

		List<List<Integer>> result = new ArrayList<>();
		for (int i = 0; i < nums.length - 2; i++) {
			if (i == 0 || nums[i] != nums[i - 1]) {
				int lower = i + 1;
				int higher = nums.length - 1;
				while (lower < higher) {
					if (nums[i] + nums[lower] + nums[higher] == 0) {
						result.add(Arrays.asList(nums[i], nums[lower], nums[higher]));
						// to eliminate same number
						while (lower < higher && nums[lower] == nums[lower+1]) {
							lower++;
						}
						while (lower < higher && nums[higher] == nums[higher-1]) {
							higher--;
						}
						lower++;
						higher--;
					} else if (nums[lower] + nums[higher] + nums[i] < 0) {
						lower++;
					} else {
						higher--;
					}
				}
			}
		}
		return result;
	}
}
