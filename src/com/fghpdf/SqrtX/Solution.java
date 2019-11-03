package com.fghpdf.SqrtX;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * https://leetcode.com/problems/sqrtx/submissions/
 * 牛顿法
 */
public class Solution {
	public int mySqrt(int x) {
		long r = x;
		while (r*r > x) {
			r = (r + x/r) / 2;
		}
		return (int) r;
	}

}
