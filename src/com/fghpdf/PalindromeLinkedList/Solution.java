package com.fghpdf.PalindromeLinkedList;

import java.util.Stack;

import com.fghpdf.ListNode;

/**
 * @author fghpdf
 * @date 2019/11/3
 *
 * https://leetcode.com/problems/palindrome-linked-list/
 * don't use stack
 * use slow and fast pointer
 * when fast is null, the slow is middle
 * then reverse slow pointer
 * two pointers move together and compare
 **/
public class Solution {
	public boolean isPalindrome(ListNode head) {
		ListNode slow = head, fast = head;
		while (fast != null && fast.next != null) {
			slow = slow.next;
			fast = fast.next.next;
		}

		if (fast != null) {
			slow = slow.next;
		}

		slow = reverse(slow);

		while (slow != null) {
			if (slow.val != head.val) {
				return false;
			}
			slow = slow.next;
			head = head.next;
		}

		return true;

	}

	private ListNode reverse(ListNode head) {
		ListNode prev = null;
		while (head != null) {
			ListNode next = head.next;
			head.next = prev;
			prev = head;
			head = next;
		}

		return prev;
	}
}
