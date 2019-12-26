package com.fghpdf.LongestIncreasingSubsequence;

/**
 * @author fghpdf
 * @date 2019/12/26
 * https://leetcode.com/problems/longest-increasing-subsequence/
 * https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
 * len = 1   :      [4], [5], [6], [3]   => tails[0] = 3
 * len = 2   :      [4, 5], [5, 6]       => tails[1] = 5
 * len = 3   :      [4, 5, 6]            => tails[2] = 6
 * (1) if x is larger than all tails, append it, increase the size by 1
 * (2) if tails[i-1] < x <= tails[i], update tails[i]
 **/
public class Solution {
	public int lengthOfLIS(int[] nums) {
		int[] tails = new int[nums.length];
		int size = 0;
		for (int x : nums) {
			int i = 0;
			int j = size;
			while (i != j) {
				int middle = (i + j) / 2;
				if (tails[middle] < x) {
					i = middle + 1;
				} else {
					j = middle;
				}
			}
			tails[i] = x;
			if (i == size) {
				size++;
			}
		}
		return size;
	}
}
