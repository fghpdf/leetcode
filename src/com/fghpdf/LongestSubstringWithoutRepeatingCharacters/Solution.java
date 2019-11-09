package com.fghpdf.LongestSubstringWithoutRepeatingCharacters;

import java.util.HashMap;
import java.util.Map;

/**
 * @author fghpdf
 * @date 2019/11/9
 *
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 * two pointer and a map to save the char position
 * first pointer is to loop string
 * second pointer is to jump to the repeat position
 * when I found repeat char, the substring is over
 * so I should start from the last char of the substring
 **/
public class Solution {
	public int lengthOfLongestSubstring(String s) {
		if (s == null || "".equals(s)) {
			return 0;
		}
		Map<Character, Integer> position = new HashMap<>(26);

		int maxLength = -1;
		for (int i = 0, repeatPosition = 0; i < s.length(); i++) {
			char c = s.charAt(i);
			if (position.get(c) != null) {
				repeatPosition = Math.max(repeatPosition, position.get(c) + 1);
				System.out.println(repeatPosition);
			}
			position.put(c, i);
			maxLength = Math.max(i - repeatPosition + 1, maxLength);
		}
		return maxLength;
	}

	public static void main(String[] args) {
		Solution sol = new Solution();
		System.out.println(sol.lengthOfLongestSubstring("abcabcdd"));
	}
}
