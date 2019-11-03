package com.fghpdf.IntersectionOfTwoLinkedLists;


/**
 * https://leetcode.com/problems/intersection-of-two-linked-lists/
 * @author fghpdf
 *
 * should read this solution: https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49785/Java-solution-without-knowing-the-difference-in-len!
 * and https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49785/Java-solution-without-knowing-the-difference-in-len!/165648
 */
public class Solution {
	public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
		if (headA == null || headB == null) {
			return null;
		}

		ListNode a = headA;
		ListNode b = headB;

		while (a != b) {
			a = a == null ? headB : a.next;
			b = b == null ? headA : b.next;
		}

		return a;
	}
}
