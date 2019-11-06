package com.fghpdf.ReverseString;

/**
 * @author fghpdf
 * @date 2019/11/6
 *
 * https://leetcode.com/problems/reverse-string/
 *
 * the question need not to use extra space, so we should change head and tail.
 **/
public class Solution {
	public void reverseString(char[] s) {
		if (s.length == 0) {
			return;
		}

		int start = 0;
		int end = s.length - 1;
		while (start < end) {
			char temp = s[start];
			s[start] = s[end];
			s[end] = temp;
			start++;
			end--;
		}
	}
}
