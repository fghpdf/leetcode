package com.fghpdf.PlusOne;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Solution {
	public int[] plusOne(int[] digits) {
		Stack<Integer> digitStack = new Stack<>();
		int carry = 1;
		for (int i = digits.length - 1; i >= 0; i--) {
			int digit = digits[i] + carry;
			if (digit >= 10) {
				carry = 1;
			} else {
				carry = 0;
			}

			digitStack.push(digit % 10);
		}
		if (carry == 1) {
			digitStack.push(1);
		}


		int[] res = new int[digitStack.size()];
		for (int i = 0;!digitStack.isEmpty();i++) {
			res[i] = digitStack.pop();
		}

		return res;
	}

	public static void main(String[] args) {
		int[] a = new int[]{9,9,9,9};
		Solution sol = new Solution();
		int[] re = sol.plusOne(a);
		for (int d:re ) {
			System.out.println(d);
		}
	}
}
