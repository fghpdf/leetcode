package com.fghpdf.FirstUniqueCharacterInAString;

import java.util.HashMap;
import java.util.Map;

/**
 * @author fghpdf
 * @date 2019/11/7
 *
 * https://leetcode.com/problems/first-unique-character-in-a-string/
 * just two loop and O(n)
 **/
public class Solution {
	public int firstUniqChar(String s) {
		if (s == null || s.length() == 0) {
			return -1;
		}

		Map<Character, Integer> isRepeat = new HashMap<>(s.length());

		for (int i = 0; i < s.length(); i++) {
			char c = s.charAt(i);
			isRepeat.put(c, isRepeat.getOrDefault(c, 0) + 1);
		}

		for (int i = 0; i < s.length(); i++) {
			char c = s.charAt(i);
			if (isRepeat.get(c) == 1) {
				return i;
			}
		}

		return -1;
	}
}
