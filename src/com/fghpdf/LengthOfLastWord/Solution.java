package com.fghpdf.LengthOfLastWord;

import java.util.List;

public class Solution {
	public int lengthOfLastWord(String s) {
		String[] words = s.split(" ");
		if (words.length == 0) {
			return 0;
		}
		String lastWord = words[words.length - 1];

		return lastWord.length();
	}

	public static void main(String[] args) {
		Solution sol = new Solution();
		int a = sol.lengthOfLastWord(" ");
		System.out.println(a);
	}
}
