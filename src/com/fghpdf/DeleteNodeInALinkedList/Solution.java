package com.fghpdf.DeleteNodeInALinkedList;

import com.fghpdf.ListNode;

/**
 * @author fghpdf
 * @date 2019/11/3
 *
 * https://leetcode.com/problems/delete-node-in-a-linked-list/
 * input only a element needs to be deleted, we have not head pointer
 * so the way is to change the node val ....
 * terrible
 **/
public class Solution {
	public void deleteNode(ListNode node) {
		node.val = node.next.val;
		node.next = node.next.next;
	}
}
