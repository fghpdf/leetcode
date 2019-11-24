package com.fghpdf.UniquePaths;

/**
 * @author fghpdf
 * @date 2019/11/24
 * https://leetcode.com/problems/unique-paths/
 * use formula about permutation and combination
 * we start from (1, 1) so all steps to target is m + n - 2
 * so we have C(All, Down) paths
 * C(All, Down) is All! / (Down!(All - Down)!)
 * C = ( (n - k + 1) * (n - k + 2) * ... * n ) / k!
 **/
public class Solution {
	public int uniquePaths(int m, int n) {
		int allSteps = m + n - 2;
		int downSteps = m - 1;

		double res = 1;
		for (int i = 1; i <= downSteps; i++) {
			res = res * (allSteps - downSteps + 1) / i;
		}
		return (int) res;
	}
}
