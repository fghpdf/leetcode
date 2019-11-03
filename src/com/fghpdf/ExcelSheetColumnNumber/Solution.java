package com.fghpdf.ExcelSheetColumnNumber;

/**
 * https://leetcode.com/problems/excel-sheet-column-number/
 * @author fghpdf
 *
 * the rule is
 * A: 26 ^ 0 * 1
 * AA: 26 ^ 1 * 1 + 26 ^ 0 * 1 = 27
 * AAA: 26 ^ 2 * 1 + 26 * 1 + 1 = 703
 */
public class Solution {

	public int titleToNumber(String s) {
		int alphaNumber;
		int result = 0;


		for (int i = 0; i < s.length(); i++) {
			char alpha = s.charAt(i);
			alphaNumber = alpha - 'A' + 1;
			result += alphaNumber * Math.pow(26, s.length() - i - 1);
		}

		return result;
	}

	public static void main(String[] args) {
		Solution sol = new Solution();
		int res = sol.titleToNumber("CAA");
		System.out.println(res);
	}
}
