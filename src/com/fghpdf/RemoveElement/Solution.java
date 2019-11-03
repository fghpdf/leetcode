package com.fghpdf.RemoveElement;

public class Solution {
    public int removeElement(int[] nums, int val) {
        int begin = 0;
        for (int i = 0; i < nums.length; i++) {
            if (val != nums[i]) {
                nums[begin] = nums[i];
                begin++;
            }
        }
        return begin;
    }

    public static void main(String[] args) {
        int[] nums = {0,1,2,2,3,0,4,2};
        Solution sol = new Solution();
        System.out.println(sol.removeElement(nums, 2));
    }
}
