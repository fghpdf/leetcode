package com.fghpdf.WiggleSortII;

import java.util.Arrays;
import java.util.Comparator;

/**
 * @author fghpdf
 * @date 2019/12/29
 * https://leetcode.com/problems/wiggle-sort-ii/
 * 没懂。。。
 * https://leetcode.com/problems/wiggle-sort-ii/discuss/77682/Step-by-step-explanation-of-index-mapping-in-Java
 **/
public class Solution {
	public void wiggleSort(int[] nums) {
		int median=findKthLargest(nums,(nums.length+1)/2);
		int odd=1;
		int even=nums.length%2==0?nums.length-2:nums.length-1;
		int[] tmpArr=new int[nums.length];
		for(int i=0;i<nums.length;i++){
			if(nums[i]>median){
				tmpArr[odd]=nums[i];
				odd+=2;
				continue;
			}
			if(nums[i]<median){
				tmpArr[even]=nums[i];
				even-=2;
				continue;
			}
		}
		while(odd<nums.length){
			tmpArr[odd]=median;
			odd+=2;
		}
		while(even>=0){
			tmpArr[even]=median;
			even-=2;
		}
		for(int i=0;i<nums.length;i++){
			nums[i]=tmpArr[i];
		}


	}

	private int findKthLargest(int[] nums, int k) {
		int[] sorted = Arrays.stream(nums).boxed()
				.sorted(Comparator.reverseOrder())
				.mapToInt(Integer::intValue)
				.toArray();

		return sorted[k - 1];
	}
}
