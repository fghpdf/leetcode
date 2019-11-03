package com.fghpdf.CountAndSay;

//https://leetcode.com/problems/count-and-say/

public class Solution {
    public String countAndSay(int n) {
        if (n == 1) {
            return "1";
        }
        String last = countAndSay(n-1);
        int lastLength = last.length();
        StringBuilder now = new StringBuilder();
        for (int i = 0; i < lastLength;) {
            char number = last.charAt(i);

            int count = 0;
            while (i + count < lastLength && last.charAt(i + count) == number) {
                count++;
            }
            now.append(count);
            now.append(number);
            i += count;
        }

        return now.toString();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.countAndSay(6));
    }
}
