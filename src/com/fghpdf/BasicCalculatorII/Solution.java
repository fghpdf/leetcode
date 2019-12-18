package com.fghpdf.BasicCalculatorII;

import java.util.Stack;

/**
 * @author fghpdf
 * @date 2019/12/18
 * https://leetcode.com/problems/basic-calculator-ii/
 * use stack to save sign
 *
 **/
public class Solution {
	public int calculate(String s) {
		if (s == null) {
			return 0;
		}
		int len = s.length();
		int result = 0;
		char sign = '+';
		Stack<Integer> resultStack = new Stack<>();
		for (int i = 0; i < len; i++) {
			char now = s.charAt(i);
			if (Character.isDigit(now)) {
				// " sum up the multi-digit number e.g. "23" -> 2*10+3
				result = result * 10 + now - '0';
			}
			if (!Character.isDigit(now) && ' ' != now || i == len - 1) {
				if (sign == '-') {
					resultStack.push(-result);
				}
				if (sign == '+') {
					resultStack.push(result);
				}
				if (sign == '*') {
					resultStack.push(resultStack.pop() * result);
				}
				if (sign == '/') {
					resultStack.push(resultStack.pop() / result);
				}
				sign = now;
				result = 0;
			}
		}

		result = 0;
		for (int i : resultStack) {
			result += i;
		}
		return result;
	}

	public static void main(String[] args) {
		Solution solution = new Solution();
		Integer a = solution.calculate("3+2*2");
		System.out.println(a);
	}
}
