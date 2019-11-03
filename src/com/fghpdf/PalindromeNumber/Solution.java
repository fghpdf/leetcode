package com.fghpdf.PalindromeNumber;

public class Solution {
    public boolean isPalindrome(int x) {
        String revrsed = new StringBuilder().append(x).reverse().toString();
        String xStr = Integer.toString(x);

        if (revrsed.equals(xStr)) {
            return true;
        }

        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.isPalindrome(12));
    }
}
