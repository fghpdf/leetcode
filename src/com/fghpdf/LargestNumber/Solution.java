package com.fghpdf.LargestNumber;

import java.util.Arrays;

/**
 * @author fghpdf
 * @date 2019/12/13
 * https://leetcode.com/problems/largest-number/
 * String s1 = "9";
 * String s2 = "31";
 *
 * String case1 =  s1 + s2; // 931
 * String case2 = s2 + s1; // 319
 *
 * we should use lager case1
 * Arrays.sort(sNums, (s1, s2) -> (s2 + s1).compareTo(s1 + s2));
 **/
public class Solution {
	public String largestNumber(int[] nums) {
		if (nums == null || nums.length == 0) {
			return "";
		}

		String[] sNums = new String[nums.length];
		for (int i = 0; i < nums.length; i++) {
			sNums[i] = String.valueOf(nums[i]);
		}
		Arrays.sort(sNums, (s1, s2) -> (s2 + s1).compareTo(s1 + s2));
		if(sNums[0].charAt(0) == '0') {
			return "0";
		}

		StringBuilder result = new StringBuilder();
		for (String sNum : sNums) {
			result.append(sNum);
		}
		return result.toString();
	}
}
