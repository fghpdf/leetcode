package com.fghpdf.ValidParentheses;

import java.util.Stack;

public class Solution {
    public boolean isValid(String s) {
        String pushParentheses = "([{";
        String popParentheses = ")]}";

        Stack<Character> parenthesesStack = new Stack<Character>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (pushParentheses.indexOf(c) != -1) {
                parenthesesStack.push(c);
            }

            if (popParentheses.indexOf(c) != -1) {
                if (parenthesesStack.isEmpty()) {
                    return false;
                }
                char pushedParent = parenthesesStack.pop();

                if (popParentheses.indexOf(c) != pushParentheses.indexOf(pushedParent)) {
                    return false;
                }
            }
        }

        if (parenthesesStack.isEmpty()) {
            return true;
        }

        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.isValid("}[}({})"));
    }
}
