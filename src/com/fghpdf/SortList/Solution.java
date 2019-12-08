package com.fghpdf.SortList;

import com.fghpdf.ListNode;

/**
 * @author fghpdf
 * @date 2019/12/8
 * https://leetcode.com/problems/sort-list/
 * merge two sorted list
 * so first to cut list and then merge
 **/
public class Solution {
	public ListNode sortList(ListNode head) {
		if (head == null || head.next == null) {
			return head;
		}

		ListNode fast = head.next;
		ListNode slow = head;

		while (fast != null && fast.next != null) {
			fast = fast.next.next;
			slow = slow.next;
		}

		// now head is end to slow
		ListNode cutSlow = slow.next;
		slow.next = null;

		return mergeTwoLists(sortList(head), sortList(cutSlow));
	}

	private ListNode mergeTwoLists(ListNode l1, ListNode l2) {
		ListNode sortedList = new ListNode(0);
		ListNode head = sortedList;

		while (l1 != null && l2 != null) {
			if (l1.val <= l2.val) {
				sortedList.next = l1;
				sortedList = sortedList.next;

				l1 = l1.next;
			} else {
				sortedList.next = l2;
				sortedList = sortedList.next;

				l2 = l2.next;
			}
		}

		if (l1 != null) {
			sortedList.next = l1;
		}

		if (l2 != null) {
			sortedList.next = l2;
		}

		return head.next;
	}
}
