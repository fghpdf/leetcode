package com.fghpdf.AddBinary;

import java.util.ArrayList;
import java.util.List;

/**
 * https://leetcode.com/problems/add-binary/
 */
public class Solution {
	public String addBinary(String a, String b) {
		StringBuilder stringBuilder = new StringBuilder();
		int carry = 0, i = a.length() - 1, j = b.length() - 1;
		while (i >= 0 || j >= 0) {
			int sum = carry;
			if (j >= 0) {
				sum += b.charAt(j--) - '0';
			}
			if (i >= 0) {
				sum += a.charAt(i--) - '0';
			}
			stringBuilder.append(sum % 2);
			carry = sum / 2;
		}
		if (carry != 0) {
			stringBuilder.append(carry);
		}
		return stringBuilder.reverse().toString();
	}
	public static void main(String[] args) {
		Solution solution = new Solution();
		System.out.println(solution.addBinary("111", "10"));
		List<Long> a = new ArrayList<>();
		a.add(Long.valueOf(1));
		a.add(Long.valueOf(2));
		a.add(Long.valueOf(3));
		List<Long> b = a.subList(0, 2);
		b.add(Long.valueOf(7));
		System.out.println(a);
	}
}
