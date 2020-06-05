package com.fghpdf.SortArrayByParity;

import java.util.Arrays;

/**
 * @author fghpdf
 * @date 2020/6/5
 * @link https://leetcode.com/problems/sort-array-by-parity/
 **/
public class Solution {
    public int[] sortArrayByParity(int[] A) {
        if (A.length == 0) {
            return A;
        }

        // two point
        int findOdd = 0;
        int findEven = A.length - 1;

        while (findOdd < findEven) {
            // find odd in left
            while (findOdd < findEven && A[findOdd] % 2 == 0) {
                findOdd++;
            }

            // find even in right
            while (findOdd < findEven && A[findEven] % 2 != 0) {
                findEven--;
            }

            // swap even and odd
            if (findOdd < findEven) {
                int temp = A[findOdd];
                A[findOdd] = A[findEven];
                A[findEven] = temp;
            }
        }

        return A;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(Arrays.toString(solution.sortArrayByParity(new int[]{3, 1, 2, 4})));
    }
}
