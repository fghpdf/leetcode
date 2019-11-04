package com.fghpdf.ValidAnagram;

import java.util.HashMap;
import java.util.Map;

/**
 * @author fghpdf
 * @date 2019/11/4
 *
 * https://leetcode.com/problems/valid-anagram/
 * the way is just to create a list for each letter in first string.
 **/
public class Solution {
	public boolean isAnagram(String s, String t) {
		if (s.length() != t.length()) {
			return false;
		}
		Map<Character, Integer> alpha = new HashMap<>(s.length());

		for (int i = 0; i < s.length(); i++) {
			alpha.merge(s.charAt(i), 1, Integer::sum);
		}

		for (int i = 0; i < t.length(); i++) {
			Integer nums = alpha.get(t.charAt(i));
			if (nums == null || nums == 0) {
				return false;
			}

			if (nums == 1) {
				alpha.remove(t.charAt(i));
			} else {
				alpha.replace(t.charAt(i), nums - 1);
			}
		}

		return alpha.size() == 0;
	}

	public static void main(String[] args) {
		Solution sol = new Solution();
		System.out.println(sol.isAnagram("", ""));
	}
}
