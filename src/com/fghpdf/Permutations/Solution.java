package com.fghpdf.Permutations;

import java.util.ArrayList;
import java.util.List;

/**
 * @author fghpdf
 * @date 2019/11/19
 * https://leetcode.com/problems/permutations/
 * It's a common backtracking pattern, choose --> explore --> unchoose
 *
 * many other backtracking questions
 * https://leetcode.com/problems/permutations/discuss/18239/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partioning)
 *
 **/
public class Solution {
	public List<List<Integer>> permute(int[] nums) {
		List<List<Integer>> list = new ArrayList<>();
		backtrack(list, new ArrayList<>(), nums);
		return list;
	}

	private void backtrack(List<List<Integer>> list, List<Integer> tempList, int[] nums) {
		if (tempList.size() == nums.length) {
			list.add(new ArrayList<>(tempList));
		} else {
			for (int num : nums) {
				if (tempList.contains(num)) {
					continue;
				}
				tempList.add(num);
				backtrack(list, tempList, nums);
				tempList.remove(tempList.size() - 1);
			}
		}
	}
}

