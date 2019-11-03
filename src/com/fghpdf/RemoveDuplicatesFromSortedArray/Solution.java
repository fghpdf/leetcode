package com.fghpdf.RemoveDuplicatesFromSortedArray;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public int removeDuplicates(int[] nums) {
        int count = 0;
        for (int n: nums) {
            if (count == 0 || n > nums[count-1]) {
                nums[count++] = n;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        List<Integer> list = new ArrayList<Integer>();
        list.add(1);
        list.add(2);
        list.add(3);
        list.add(4);

        list.subList(2,3).clear();

        System.out.println(list.size());
    }
}
