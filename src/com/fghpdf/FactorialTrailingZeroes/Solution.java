package com.fghpdf.FactorialTrailingZeroes;

/**
 * https://leetcode.com/problems/factorial-trailing-zeroes/
 * @author fghpdf
 *
 * the zero is come from 5 * 2, and 2 is alway exists
 * so we just find how many 5 haves
 * So first we add n/5.
 * Wait, we are missing 5X5, 2X5X5..., so we add n/25 (why not count as two 5's for each , because one is already counted in n/5).
 * Wait, we are missing 5X5X5, 2X5X5X5..., so we add n/125.
 * Thus, count = n/5 + n/25 + n/125 + ... + 0
 */
public class Solution {
	public int trailingZeroes(int n) {
		if (n == 0) {
			return 0;
		}

		return n / 5 + trailingZeroes(n / 5);
	}
}
