package com.fghpdf.MinStack;

import java.util.Stack;

/**
 * https://leetcode.com/problems/min-stack/
 * https://leetcode.com/problems/min-stack/discuss/49014/Java-accepted-solution-using-one-stack
 *
 * The two stack method is use another stack to save min
 * minStack push element when x <= min
 * if origin stack pop min, minStack pop too
 * getMin is minStack top
 */
public class Solution {
	private int min = Integer.MAX_VALUE;
	private Stack<Integer> stack = new Stack<>();

	// notice first push the second min,then push first min
	// so a stack like { MAX_VALUE, 1, 1, 2, 1, -3, 4 }
	public void push(int x) {
		if (x <= min) {
			stack.push(min);
			min = x;
		}
		stack.push(x);
	}

	// when found pop is min, the second min must be next one
	public void pop() {
		if (stack.pop() == min) {
			min = stack.pop();
		}
	}

	public int top() {
		return stack.peek();
	}

	public int getMin() {
		return min;
	}
}
