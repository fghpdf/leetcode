package com.fghpdf.ValidPalindrome;

/**
 * https://leetcode.com/problems/valid-palindrome/
 * @author fghpdf
 *
 * sample question, we can loop the string to filter the alphanumeric characters
 * and compare the s[i] == s[j]
 *
 * Also we can use regular to replace all nonaplha characters
 * s.replaceAll("[^A-Za-z0-9]", "").toLowerCase();
 */
public class Solution {
	public boolean isPalindrome(String s) {
		char[] chars = s.toCharArray();

		for (int i = 0, j = chars.length - 1; i < j;) {
			// if found a char is't alpha then continue
			if (!Character.isLetterOrDigit(chars[i])) {
				i++;
				continue;
			}

			if (!Character.isLetterOrDigit(chars[j])) {
				j--;
				continue;
			}

			if (Character.toLowerCase(chars[i++]) != Character.toLowerCase(chars[j--])) {
				return false;
			}
		}

		return true;
	}

	public static void main(String[] args) {
		Solution solution = new Solution();
		System.out.println(solution.isPalindrome("A man, a plan, a canal: Panama"));
	}
}
