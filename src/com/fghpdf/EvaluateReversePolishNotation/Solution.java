package com.fghpdf.EvaluateReversePolishNotation;

import java.util.Stack;

/**
 * @author fghpdf
 * @date 2019/12/9
 * 后缀表达式
 * loop whole string
 * if it is number push stack
 * if it is operator, pop two number to calculate and then push result to stack
 **/
public class Solution {
	public int evalRPN(String[] tokens) {
		Stack<Integer> integerStack = new Stack<>();
		for(String s : tokens) {
			if("+".equals(s)) {
				integerStack.add(integerStack.pop() + integerStack.pop());
			} else if ("/".equals(s)) {
				Integer divisor = integerStack.pop();
				Integer dividend = integerStack.pop();
				integerStack.add(dividend / divisor);
			} else if ("*".equals(s)) {
				integerStack.add(integerStack.pop() * integerStack.pop());
			} else if ("-".equals(s)) {
				Integer subtractor = integerStack.pop();
				Integer minuend = integerStack.pop();
				integerStack.add(minuend - subtractor);
			} else {
				integerStack.add(Integer.parseInt(s));
			}
		}
		return integerStack.pop();
	}
}
