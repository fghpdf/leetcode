package com.fghpdf.InsertDeleteGetRandom;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Random;

/**
 * @author fghpdf
 * @date 2020/1/27
 * @link https://leetcode.com/problems/insert-delete-getrandom-o1/
 * random need nums size
 * to prove O(1) so use HashMap to save size
 **/
class RandomizedSet {
	private ArrayList<Integer> nums;
	private HashMap<Integer, Integer> locs;
	private Random random = new Random();

	/** Initialize your data structure here. */
	public RandomizedSet() {
		nums = new ArrayList<>();
		locs = new HashMap<>();
	}

	/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
	public boolean insert(int val) {
		boolean contain = locs.containsKey(val);
		if (contain) {
			return false;
		}

		locs.put(val, nums.size());
		nums.add(val);
		return true;
	}

	/** Removes a value from the set. Returns true if the set contained the specified element. */
	public boolean remove(int val) {
		boolean contain = locs.containsKey(val);
		if (!contain) {
			return false;
		}

		int loc = locs.get(val);
		if (loc < nums.size() - 1) {
			int lastOne = nums.get(nums.size() - 1);
			nums.set(loc, lastOne);
			locs.put(lastOne, loc);
		}

		locs.remove(val);
		nums.remove(nums.size() - 1);
		return true;
	}

	/** Get a random element from the set. */
	public int getRandom() {
		return nums.get(random.nextInt(nums.size()));
	}
}

