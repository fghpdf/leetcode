package com.fghpdf.PalindromePartitioning;

import java.util.ArrayList;
import java.util.List;

/**
 * @author fghpdf
 * @date 2019/12/5
 * https://leetcode.com/problems/palindrome-partitioning/
 * dfs
 * aab -> a -> tempList -> ab -> a -> tempList -> b -> tempList -> result
 * tempList remove all
 * aab -> aa -> tempList -> b -> false
 **/
public class Solution {
	public List<List<String>> partition(String s) {
		List<List<String>> result = new ArrayList<>();
		List<String> tempList = new ArrayList<>();
		dfs(s, 0, tempList, result);
		return result;
	}

	private void dfs(String s, int pos, List<String> tempList, List<List<String>> res) {
		if (pos == s.length()) {
			res.add(new ArrayList<>(tempList));
		} else {
			for (int i = pos; i < s.length(); i++) {
				if (isPalindrome(s, pos, i)) {
					tempList.add(s.substring(pos, i + 1));
					dfs(s, i + 1, tempList, res);
					tempList.remove(tempList.size() - 1);
				}
			}
		}
	}

	private boolean isPalindrome(String s, int low, int high) {
		while (low < high) {
			if (s.charAt(low++) != s.charAt(high--)) {
				return false;
			}
		}
		return true;
	}

	public static void main(String[] args) {
		Solution solution = new Solution();
		System.out.println(solution.partition("aabc"));
	}
}
