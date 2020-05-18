package com.fghpdf.LongestPalindromicSubstring;

/**
 * @author fghpdf
 * @date 2019/11/9
 * https://leetcode.com/problems/longest-palindromic-substring/
 * my way is slow
 * discuss has a way to extend to search
 *
 **/
public class Solution {
	public String longestPalindrome(String s) {
		if (s.length() == 0) {
			return s;
		}

		int max = 0;
		String result = "";
		for (int i = s.length() - 1; i >= 0; i--) {
			for (int j = 0; j < s.length();j++) {
				if (i - j + 1 <= max) {
					continue;
				}
				String sub = s.substring(j, i + 1);
				if (isPalindrome(sub)) {
					max = sub.length();
					result = sub;
				}
			}
		}
		return result;
	}

	private boolean isPalindrome(String s) {
		char[] chars = s.toCharArray();

		for (int i = 0, j = chars.length - 1; i < j;) {
			if (Character.toLowerCase(chars[i++]) != Character.toLowerCase(chars[j--])) {
				return false;
			}
		}

		return true;
	}

	private int position, maxLength;

	private String lo2(String s) {
		int len = s.length();
		if (len < 2) {
			return s;
		}

		for (int i = 0; i < len-1; i++) {
			extendPalindrome(s, i, i);
			extendPalindrome(s, i, i+1);
		}
		return s.substring(position, position + maxLength);
	}

	private void extendPalindrome(String s, int left, int right) {
		while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
			left--;
			right++;
		}

		// left + 1 is palindrome start point
		// left and right is palindrome extra element so
		// right - left + 1 - 2
		if (maxLength < right - left - 1) {
			position = left + 1;
			maxLength = right - left - 1;
		}
	}



	public static void main(String[] args) {
		Solution sol = new Solution();
		System.out.println(sol.lo2("babad"));
	}
}
