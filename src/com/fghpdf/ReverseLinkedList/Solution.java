package com.fghpdf.ReverseLinkedList;

/**
 * @author fghpdf
 * @date 2019/11/2
 *
 * https://leetcode.com/problems/reverse-linked-list/#
 * remember it !
 * https://leetcode.com/problems/reverse-linked-list/discuss/58125/In-place-iterative-and-recursive-Java-solution/59714
 **/
public class Solution {
	public ListNode reverseList(ListNode head) {
		ListNode result = null;

		while (head != null) {
			ListNode temp = head.next;
			head.next = result;
			result = head;
			head = temp;
		}

		return result;
	}
}
