package com.fghpdf.SortColors;

/**
 * @author fghpdf
 * @date 2019/11/26
 * https://leetcode.com/problems/sort-colors/
 *
 * two steps is easy, count the number of color
 * and overwrite array
 *
 * one step uses two pointer
 * low ensure 0, high ensure 2
 * when u exchange two element, low or high can change
 **/
public class Solution {
	public void sortColors(int[] nums) {
		int[] colorNumbers = new int[3];

		for (int num : nums) {
			switch (num) {
				case 0:
					colorNumbers[0]++;
					break;
				case 1:
					colorNumbers[1]++;
					break;
				case 2:
					colorNumbers[2]++;
				default:
					break;
			}
		}

		for (int i = 0; i < nums.length; i++) {
			if (colorNumbers[0] > 0) {
				nums[i] = 0;
				colorNumbers[0]--;
				continue;
			}

			if (colorNumbers[1] > 0) {
				nums[i] = 1;
				colorNumbers[1]--;
				continue;
			}

			if (colorNumbers[2] > 0) {
				nums[i] = 2;
				colorNumbers[2]--;
			}
		}

	}

	public void oneStepSortColors(int[] A) {
		if (A==null || A.length<2) {
			return;
		}
		int low = 0;
		int high = A.length-1;
		for(int i = low; i<=high;) {
			if(A[i]==0) {
				// swap A[i] and A[low] and i,low both ++
				int temp = A[i];
				A[i] = A[low];
				A[low]=temp;
				i++;low++;
			}else if(A[i]==2) {
				//swap A[i] and A[high] and high--;
				int temp = A[i];
				A[i] = A[high];
				A[high]=temp;
				high--;
			}else {
				i++;
			}
		}
	}
}
