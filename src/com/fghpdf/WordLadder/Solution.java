package com.fghpdf.WordLadder;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;

/**
 * @author fghpdf
 * @date 2019/12/4
 * https://leetcode.com/problems/word-ladder/
 * BFS
 * to change letter many times and find the result
 **/
public class Solution {
	public int ladderLength(String beginWord, String endWord, List<String> wordList) {
		Set<String> dict = new HashSet<>(wordList);
		Set<String> visited = new HashSet<>();
		Queue<String> q = new LinkedList<>();

		q.offer(beginWord);
		for (int len = 1; !q.isEmpty() ; len++) {
			for (int i = q.size(); i > 0 ; i--) {
				String w = q.poll();
				if (w.equals(endWord)) {
					return len;
				}

				for (int j = 0; j < w.length(); j++) {
					char[] word = w.toCharArray();
					for (char c = 'a'; c <= 'z'; c++) {
						if (c == w.charAt(j)) {
							continue;
						}

						word[j] = c;
						String newWord = String.valueOf(word);
						if (dict.contains(newWord) && visited.add(newWord)) {
							q.offer(newWord);
						}
					}
				}
			}
		}
		return 0;
	}
}
