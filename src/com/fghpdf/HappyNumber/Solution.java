package com.fghpdf.HappyNumber;

/**
 * @author fghpdf
 * @date 2019/10/30
 * https://leetcode.com/problems/happy-number/
 *
 * end at cycle, so we should use the Floyd Cycle detection algorithm.
 * a fast pointer, and a slow one.
 * It's a cycle when they met.
 **/
public class Solution {
	public boolean isHappy(int n) {
		int slow = n;
		int fast = n;

		do {
			slow = digitSquareSum(slow);
			fast = digitSquareSum(fast);
			fast = digitSquareSum(fast);
		} while (slow != fast);

		return slow == 1;
	}

	private int digitSquareSum(int n) {
		int sum = 0;
		int tmp;

		while (n > 0) {
			tmp = n % 10;
			sum += tmp * tmp;
			n /= 10;
		}
		return sum;
	}
}
