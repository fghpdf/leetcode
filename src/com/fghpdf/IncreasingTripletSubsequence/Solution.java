package com.fghpdf.IncreasingTripletSubsequence;

/**
 * @author fghpdf
 * @date 2020/1/2
 * @link https://leetcode.com/problems/increasing-triplet-subsequence/
 * subsequence is a number has smaller and bigger number in array
 * update big only if greater than small but smaller than big
 **/
public class Solution {
	public boolean increasingTriplet(int[] nums) {
		int small = Integer.MAX_VALUE;
		int big = Integer.MAX_VALUE;
		for (int num : nums) {
			if (num <= small) {
				small = num;
			} else if (num <= big) {
				big = num;
			} else {
				return true;
			}
		}
		return false;
	}

	public static void main(String[] args) {
		Solution solution = new Solution();
		System.out.println(solution.increasingTriplet(new int[]{1, 3, 0, 6}));
	}
}
