package com.fghpdf.ReversePairs;

import java.util.Arrays;

/**
 * @author fghpdf
 * @date 2020/6/7
 * @link https://leetcode.com/problems/reverse-pairs/#/description
 **/
public class Solution {
    public int reversePairs(int[] nums) {
        return mergeSort(nums, 0, nums.length - 1);
    }

    private int mergeSort(int[] nums, int start, int end) {
        if (start >= end) {
            return 0;
        }

        int mid = start + (end - start) / 2;
        int result = mergeSort(nums, start, mid) + mergeSort(nums, mid + 1, end);
        for (int left = start, right = mid + 1; left <= mid; left++) {
            // find reverse pairs
            while (right <= end && nums[left] / 2.0 > nums[right]) {
                right++;
            }

            result += right - (mid + 1);
        }
        Arrays.sort(nums, start, end + 1);
        return result;
    }
}
