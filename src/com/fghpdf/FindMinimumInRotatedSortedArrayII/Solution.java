package com.fghpdf.FindMinimumInRotatedSortedArrayII;

/**
 * @author fghpdf
 * @date 2020/6/14
 * @link https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
 **/
public class Solution {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        // loop [left, right)
        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] < nums[right]) {
                // min is in left
                right = mid;
            } else if (nums[mid] > nums[right]) {
                // min is in right
                left = mid + 1;
            } else {
                // left and right is same
                right--;
            }
        }

        // left == right == min
        return nums[left];
    }
}
