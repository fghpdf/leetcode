package com.fghpdf.CopyListWithRandomPointer;

import java.util.HashMap;
import java.util.Map;

/**
 * @author fghpdf
 * @date 2019/12/7
 * https://leetcode.com/problems/copy-list-with-random-pointer/
 * copy all nodes to map
 * assign next and random
 **/
public class Solution {
	public Node copyRandomList(Node head) {
		if (head == null) {
			return null;
		}

		Map<Node, Node> nodeMap = new HashMap<>(16);

		Node node = head;
		while (node != null) {
			nodeMap.put(node, new Node(node.val, node.next, node.random));
			node = node.next;
		}

		node = head;
		while (node != null) {
			nodeMap.get(node).next = nodeMap.get(node.next);
			nodeMap.get(node).random = nodeMap.get(node.random);
			node = node.next;
		}

		return nodeMap.get(head);
	}
}
