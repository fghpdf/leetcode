package com.fghpdf.FizzBuzz;

import java.util.ArrayList;
import java.util.List;

/**
 * @author fghpdf
 * @date 2019/11/7
 *
 * https://leetcode.com/problems/fizz-buzz/
 * easy question..
 **/
public class Solution {
	public List<String> fizzBuzz(int n) {
		List<String> result = new ArrayList<>();
		for (int i = 1; i <= n; i++) {
			if (i % 3 == 0 && i % 5 == 0) {
				result.add("FizzBuzz");
				continue;
			}

			if (i % 3 == 0) {
				result.add("Fizz");
				continue;
			}

			if (i % 5 == 0) {
				result.add("Buzz");
				continue;
			}

			result.add(String.valueOf(i));
		}

		return result;
	}
}
