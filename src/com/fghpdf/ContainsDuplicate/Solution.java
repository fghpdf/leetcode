package com.fghpdf.ContainsDuplicate;

import java.util.HashSet;
import java.util.Set;

/**
 * @author fghpdf
 * @date 2019/11/2
 *
 * https://leetcode.com/problems/contains-duplicate/
 **/
public class Solution {
	public boolean containsDuplicate(int[] nums) {
		Set numsSet = new HashSet();
		for (int num : nums) {
			if (!numsSet.add(num)) {
				return true;
			}
		}
		return false;
	}
}
