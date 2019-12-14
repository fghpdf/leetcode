package com.fghpdf.CourseSchedule;

import java.util.LinkedList;
import java.util.Queue;

/**
 * @author fghpdf
 * @date 2019/12/14
 * https://leetcode.com/problems/course-schedule/
 * 没懂！
 * https://youtu.be/rG2-_lgcZzo
 **/
public class Solution {
	public boolean canFinish(int numCourses, int[][] prerequisites) {
		// i -> j
		int[][] matrix = new int[numCourses][numCourses];
		int[] indegree = new int[numCourses];

		for (int[] prerequisite : prerequisites) {
			int ready = prerequisite[0];
			int pre = prerequisite[1];
			if (matrix[pre][ready] == 0) {
				//duplicate case
				indegree[ready]++;
			}
			matrix[pre][ready] = 1;
		}

		int count = 0;
		Queue<Integer> queue = new LinkedList();
		for (int i=0; i<indegree.length; i++) {
			if (indegree[i] == 0) {
				queue.offer(i);
			}
		}
		while (!queue.isEmpty()) {
			int course = queue.poll();
			count++;
			for (int i=0; i<numCourses; i++) {
				if (matrix[course][i] != 0) {
					if (--indegree[i] == 0) {
						queue.offer(i);
					}
				}
			}
		}
		return count == numCourses;
	}
}
