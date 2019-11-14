package com.fghpdf.LetterCombinationsOfAPhoneNumber;

import java.util.LinkedList;
import java.util.List;

/**
 * @author fghpdf
 * @date 2019/11/14
 * https://leetcode.com/problems/letter-combinations-of-a-phone-number/
 *
 * FIFO
 * we first build a queue to save letter
 * when first letter pushed into queue, we should remove it and get it and then
 * loop next char array
 * like a -> queue
 * remove a <- queue
 * a + d -> queue
 *
 * notice the judge is queue.peek().length == i
 * i is the letter position number
 * like before first letter join, the i is 0, the queue peek is empty string
 **/
public class Solution {
	public List<String> letterCombinations(String digits) {
		LinkedList<String> result = new LinkedList<>();
		if (digits.isEmpty()) {
			return result;
		}

		String[] digitsMap = new String[]{"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
		result.add("");
		for (int i = 0; i < digits.length(); i++) {
			int x = Character.getNumericValue(digits.charAt(i));
			while (result.peek().length() == i) {
				String temp = result.remove();
				for (char s : digitsMap[x].toCharArray()) {
					result.add(temp + s);
				}
			}
		}
		return result;
	}

	public static void main(String[] args) {
		Solution sol = new Solution();
		System.out.println(sol.letterCombinations("235"));
	}
}
