package com.fghpdf.IntersectionOfTwoArraysII;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/**
 * @author fghpdf
 * @date 2019/11/6
 *
 * https://leetcode.com/problems/intersection-of-two-arrays-ii/
 * the example will mislead you, make you think it needs adjacent numbers
 * but actually it just needs the repeat numbers
 **/
public class Solution {
	public int[] intersect(int[] nums1, int[] nums2) {
		HashMap<Integer, Integer> map = new HashMap<>(16);
		List<Integer> result = new ArrayList<>();

		for (int value : nums1) {
			map.put(value, map.getOrDefault(value, 0) + 1);
		}

		for (int value : nums2) {
			if (map.get(value) != null && map.get(value) > 0) {
				result.add(value);
				map.put(value, map.get(value) - 1);
			}
		}

		return result.stream().mapToInt(Integer::intValue).toArray();
	}
}
