package com.fghpdf.WordBreak;

import java.util.List;

/**
 * @author fghpdf
 * @date 2019/12/7
 * https://leetcode.com/problems/word-break/
 * isSubWordBreak[i] stands whether subString(0, i) is word break.
 * subString(0, 0) sets true
 **/
public class Solution {
	public boolean wordBreak(String s, List<String> wordDict) {
		boolean[] isSubWordBreak = new boolean[s.length() + 1];

		isSubWordBreak[0] = true;

		for (int i = 1; i <= s.length(); i++) {
			for (int j = 0; j < i; j++) {
				if (isSubWordBreak[j] && wordDict.contains(s.substring(j, i))) {
					isSubWordBreak[i] = true;
					break;
				}
			}
		}

		return isSubWordBreak[s.length()];
	}
}
