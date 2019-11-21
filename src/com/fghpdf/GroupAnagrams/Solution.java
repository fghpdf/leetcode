package com.fghpdf.GroupAnagrams;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @author fghpdf
 * @date 2019/11/21
 * https://leetcode.com/problems/group-anagrams/
 * my way is too slow
 * sort can be replace
 * int[] arr = new int[26];
 * for(int i = 0;i<s.length();i++){
 *     arr[s.charAt(i) - 'a']++;
 * }
 **/
public class Solution {
	public List<List<String>> groupAnagrams(String[] strs) {
		List<List<String>> result = new ArrayList<>();

		Map<String, Integer> resultPosition = new HashMap<>(strs.length);

		for (String str : strs) {
			char[] tempArray = str.toCharArray();
			Arrays.sort(tempArray);

			Integer position = resultPosition.get(Arrays.toString(tempArray));
			if (position == null) {
				result.add(new ArrayList<>(Collections.singletonList(str)));
				resultPosition.put(Arrays.toString(tempArray), result.size() - 1);
			} else {
				result.get(position).add(str);
			}
		}

		return result;
	}

	public static void main(String[] args) {
		Solution sol = new Solution();
		String[] strs = new String[]{"eat", "tea", "tan", "ate", "nat", "bat"};
		System.out.println(sol.groupAnagrams(strs));
	}
}
