package com.fghpdf.RemoveNthNodeFromEndOfList;

import com.fghpdf.ListNode;

/**
 * @author fghpdf
 * @date 2019/11/15
 * https://leetcode.com/problems/remove-nth-node-from-end-of-list/
 * fast and slow pointer
 * so easy!
 **/
public class Solution {
	public ListNode removeNthFromEnd(ListNode head, int n) {
		ListNode fast = head;
		ListNode slow = head;

		if (head == null) {
			return head;
		}

		while (fast != null && n != 0) {
			fast = fast.next;
			n--;
		}

		if (fast == null) {
			return head.next;
		}

		while (fast.next != null) {
			fast = fast.next;
			slow = slow.next;
		}

		slow.next = slow.next.next;
		return head;
	}
}
