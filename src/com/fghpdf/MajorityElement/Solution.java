package com.fghpdf.MajorityElement;

import java.util.HashMap;
import java.util.Map;

/**
 * https://leetcode.com/problems/majority-element/
 * @author fghpdf
 *
 * but my solution use O(n) space
 * the less space is here:https://leetcode.com/problems/majority-element/discuss/51613/O(n)-time-O(1)-space-fastest-solution
 */
public class Solution {
	public int majorityElement(int[] nums) {
		Map<Integer, Integer> apperTimes = new HashMap<>(nums.length);

		for (int i = 0; i < nums.length; i++) {
			int times = apperTimes.getOrDefault(nums[i], 0);
			if (times >= nums.length / 2) {
				return nums[i];
			}

			apperTimes.put(nums[i], times + 1);
		}

		return nums[0];
	}
}
