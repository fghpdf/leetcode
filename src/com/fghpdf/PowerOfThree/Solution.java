package com.fghpdf.PowerOfThree;

/**
 * @author fghpdf
 * @date 2019/11/6
 *
 * https://leetcode.com/problems/power-of-three/
 * 3 ^ 20 is bigger than int,so 3 ^ 19 % n == 0
 **/
public class Solution {
	public boolean isPowerOfThree(int n) {
		return (n > 0 && Math.pow(3, 19) % n == 0);
	}
}
