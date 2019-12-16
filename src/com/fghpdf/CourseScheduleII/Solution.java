package com.fghpdf.CourseScheduleII;

import java.util.ArrayList;
import java.util.List;

/**
 * @author fghpdf
 * @date 2019/12/16
 * https://leetcode.com/problems/course-schedule-ii/
 * TODO: 看下面的文章
 * https://leetcode.com/problems/course-schedule-ii/discuss/59317/Two-AC-solution-in-Java-using-BFS-and-DFS-with-explanation/164558
 **/
public class Solution {
	private int n = 0;

	public int[] findOrder(int numCourses, int[][] prerequisites) {
		int[] result = new int[numCourses];
		Course[] courses = new Course[numCourses];
		for (int i = 0; i < numCourses; i++) {
			courses[i] = new Course(i);
		}
		for (int[] prerequisite : prerequisites) {
			courses[prerequisite[0]].add(courses[prerequisite[1]]);
		}
		for (int i = 0; i < numCourses; i++) {
			if (isCyclic(courses[i], result)) {
				return new int[0];
			}
		}
		return result;
	}

	private boolean isCyclic(Course cur, int[] result) {
		if (cur.tested) {
			return false;
		}
		if (cur.visited) {
			return true;
		}
		cur.visited = true;
		for (Course c : cur.pre) {
			if (isCyclic(c, result)) {
				return true;
			}
		}
		cur.tested = true;
		result[n++] = cur.number;
		return false;
	}

	static class Course {
		boolean visited = false;
		boolean tested = false;
		int number;
		List<Course> pre = new ArrayList<>();
		Course(int i) {
			number = i;
		}
		public void add(Course c) {
			pre.add(c);
		}
	}
}
