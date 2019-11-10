package com.fghpdf.StringToInteger;

/**
 * @author fghpdf
 * @date 2019/11/10
 * https://leetcode.com/problems/string-to-integer-atoi/
 *
 * if else practice
 **/
public class Solution {
	public int myAtoi(String str) {
		str = str.trim();
		if (str.length() == 0) {
			return 0;
		}
		if (!isValid(str)) {
			return 0;
		}

		int start = 0;
		char sign = str.charAt(0);
		if (sign == '+' || sign == '-') {
			start = 1;
		}

		for (int i = start; i < str.length(); i++) {
			char c = str.charAt(i);
			if (!Character.isDigit(c)) {
				str = str.substring(0, i);
				break;
			}
		}

		try {
			return Integer.parseInt(str);
		} catch (NumberFormatException error) {
			if (sign == '+' || Character.isDigit(sign)) {
				return 2147483647;
			}

			if (sign == '-') {
				return -2147483648;
			}
		}

		return 0;
	}

	private boolean isValid(String str) {
		char c1 = str.charAt(0);

		if (Character.isLetter(c1)) {
			return false;
		}

		if (Character.isDigit(c1)) {
			return true;
		}

		if ('+' == c1 || '-' == c1) {
			if (str.length() < 2) {
				return false;
			}
			char c2 = str.charAt(1);
			return Character.isDigit(c2);
		}

		return false;
	}

	public static void main(String[] args) {
		Solution sol = new Solution();
		System.out.println(sol.myAtoi("20000000000000000000"));
	}
}
