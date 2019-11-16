package com.fghpdf.GenerateParentheses;

import java.util.ArrayList;
import java.util.List;

/**
 * @author fghpdf
 * @date 2019/11/16
 * https://leetcode.com/problems/generate-parentheses/
 *
 * try to add ( and when we add ( success, we can add )
 * when we try add all ( and then try to add )
 * DFS
 **/
public class Solution {
	public List<String> generateParenthesis(int n) {
		List<String> result = new ArrayList<>();
		recursiveGenerate(result, "", 0, 0, n);
		return result;
	}

	private void recursiveGenerate(List<String> result, String str, int open, int close, int max) {
		if (str.length() == max * 2) {
			result.add(str);
			return;
		}

		// try to add (
		if (open < max) {
			recursiveGenerate(result, str + "(", open + 1, close, max);
		}

		// try to add )
		if (close < open) {
			recursiveGenerate(result, str + ")", open, close + 1, max);
		}
	}

	public static void main(String[] args) {
		Solution solution = new Solution();
		System.out.println(solution.generateParenthesis(3));
	}
}
