package com.fghpdf.LinkedListCycle;

/**
 * https://leetcode.com/problems/linked-list-cycle/
 * @author fghpdf
 *
 * the problem wants to determine a list have cycle.
 * In fact, pos is answer
 *
 * a good solution is two pointer, fast and slow.
 * fast moves two steps, the slow moves only one.
 * if fast == slow, the cycle is true.
 */
public class Solution {
	public boolean hasCycle(ListNode head) {
		if (head == null) {
			return false;
		}

		ListNode runner = head;
		ListNode walker = head;

		// runner includes walker
		while (runner.next != null && runner.next.next != null) {
			walker = walker.next;
			runner = runner.next.next;
			if (runner == walker) {
				return true;
			}
		}

		return false;
	}
}
