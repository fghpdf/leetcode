package com.fghpdf.SuperPow;

import java.util.Arrays;

/**
 * @author fghpdf
 * @date 2020/5/27
 * @link https://leetcode.com/problems/super-pow/
 **/
public class Solution {
    private final int model = 1337;

    public int superPow(int a, int[] b) {
        if (b.length == 0) {
            return 1;
        }

        // last element
        int last = b[b.length - 1];

        // Recursive
        int firstPart = myPow(a, last);
        int secondPart = myPow(superPow(a, Arrays.copyOf(b, b.length - 1)), 10);

        return firstPart * secondPart % model;
    }

    private int myPow(int a, int power) {
        // odd a^b = a * a ^ b -1
        // even a^b = (a ^ b / 2) ^ 2

        if (power == 0) {
            return 1;
        }
        // (a % k)(b % k) = a * b % k
        a %= model;

        if (power % 2 == 1) {
            return (a * myPow(a, power - 1)) % model;
        } else {
            int sub = myPow(a, power / 2);
            return (sub * sub) % model;
        }
    }
}
