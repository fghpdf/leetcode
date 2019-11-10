package com.fghpdf.ContainerWithMostWater;

/**
 * @author fghpdf
 * @date 2019/11/10
 * https://leetcode.com/problems/container-with-most-water/submissions/
 *
 * because the shorter vertical line decide the area
 * so when you find left < right, area = left * length
 * the bigger area may be appear left, it can make right line to take effect
 **/
public class Solution {
	public int maxArea(int[] height) {
		int result = 0;

		int left = 0;
		int right = height.length - 1;

		while (left < right ) {
			result = Math.max(result, (right - left) * Math.min(height[left], height[right]));
			if (height[left] < height[right]) {
				left++;
			} else {
				right--;
			}
		}
		return result;
	}

	public static void main(String[] args) {
		Solution sol = new Solution();
		int[] a = {1,8,6,2,5,4,8,3,7};
		System.out.println(sol.maxArea(a));
	}
}
