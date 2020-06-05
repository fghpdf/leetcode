package com.fghpdf.ValidateStackSequences;

import java.util.Stack;

/**
 * @author fghpdf
 * @date 2020/6/5
 * @link https://leetcode.com/problems/validate-stack-sequences/
 **/
public class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        Stack<Integer> stack = new Stack<>();
        int popIndex = 0;
        for (int num : pushed) {
            stack.push(num);
            // pop from popped
            while (!stack.isEmpty() && stack.peek() == popped[popIndex]) {
                stack.pop();
                popIndex++;
            }
        }

        return stack.isEmpty();
    }
}
