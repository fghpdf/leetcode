package com.fghpdf.ProductOfArrayExceptSelf;

import java.util.Arrays;

/**
 * @author fghpdf
 * @date 2019/12/21
 * https://leetcode.com/problems/product-of-array-except-self/
 * no division
 * so we can production of left then right
 **/
public class Solution {
	public int[] productExceptSelf(int[] nums) {
		int product = 1;
		int zeroCount = 0;
		for (int num : nums) {
			if (num == 0) {
				if (++zeroCount >= 2) {
					product = 0;
					break;
				}
				continue;
			}
			product *= num;
		}

		int[] result = new int[nums.length];
		for (int i = 0; i < nums.length; i++) {
			if (zeroCount >= 1) {
				result[i] = nums[i] == 0 ? product : 0;
				continue;
			}

			result[i] = product / nums[i];
		}

		return result;
	}

	private int[] noDivison(int[] nums) {
		int n = nums.length;
		int[] res = new int[n];
		res[0] = 1;
		for (int i = 1; i < n; i++) {
			res[i] = res[i - 1] * nums[i - 1];
		}
		int right = 1;
		for (int i = n - 1; i >= 0; i--) {
			res[i] *= right;
			right *= nums[i];
		}
		return res;
	}

	public static void main(String[] args) {
		Solution solution = new Solution();
		System.out.println(Arrays.toString(solution.productExceptSelf(new int[]{0, 0})));
	}
}
