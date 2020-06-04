package com.fghpdf.SingleNumberIII;

/**
 * @author fghpdf
 * @date 2020/6/4
 * @link https://leetcode.com/problems/single-number-ii/
 **/
public class Solution {
    public int[] singleNumber(int[] nums) {
        int[] result = new int[2];
        if (nums.length == 0) {
            return result;
        }

        // step 1
        // get xor result
        int xorResult = 0;
        for (int num : nums) {
            xorResult ^= num;
        }

        // step 2
        // get mask like 0010
        int mask = getMask(xorResult);

        // step 3
        // the number will divide into two group by mask
        // the result will also in two group
        for (int num : nums) {
            if ((mask & num) == 0) {
                result[0] ^= num;
            } else {
                result[1] ^= num;
            }
        }

        return result;
    }

    private int getMask(int num){
        int mask = -num;
        mask &= num;
        return mask;
    }


}
