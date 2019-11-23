package com.fghpdf.JumpGame;

/**
 * @author fghpdf
 * @date 2019/11/23
 * https://leetcode.com/problems/jump-game/
 * my way is O(n), slow
 * the best way is
 * for (int reach = 0; i < n && i <= reach; ++i)
 *         reach = max(i + A[i], reach);
 * and then judge i == n
 **/
public class Solution {
	public boolean canJump(int[] nums) {
		if (nums.length == 1) {
			return true;
		}
		int unJumpZeroPosition = -1;
		for (int i = nums.length - 1; i >= 0; i--) {
			if (unJumpZeroPosition == -1 && nums[i] == 0) {
				unJumpZeroPosition = i;
				if (i == 0) {
					return false;
				}
				continue;
			}

			if (unJumpZeroPosition != -1 && unJumpZeroPosition - i + 1 <= nums[i]) {
				unJumpZeroPosition = -1;
			}

			if (unJumpZeroPosition != -1 && unJumpZeroPosition - i <= nums[i] && unJumpZeroPosition == nums.length - 1) {
				unJumpZeroPosition = -1;
			}

			if (unJumpZeroPosition != -1 && unJumpZeroPosition + 1 > nums[i] && i == 0) {
				return false;
			}
		}
		return true;
	}

	public static void main(String[] args) {
		Solution solution = new Solution();
		int[] nums = new int[]{1, 1, 1, 1, 0};
		System.out.println(solution.canJump(nums));
		nums = new int[]{0, 1};
		System.out.println(solution.canJump(nums));
		nums = new int[]{2, 0, 0};
		System.out.println(solution.canJump(nums));

	}
}
