package com.fghpdf.LRUCache;

import java.util.HashMap;
import java.util.Map;

/**
 * @author fghpdf
 * @date 2019/12/8
 * https://leetcode.com/problems/lru-cache/
 * HashMap to save key-value
 * double linked list to save sequence
 * when update key-value, move node to head next
 * just change node head prev and next pointer
 *
 * https://www.youtube.com/watch?v=S6IfqDXWa10
 **/
public class LRUCache {
	final Node head = new Node(0, 0);
	final Node tail = new Node(0, 0);
	final Map<Integer, Node> nodeMap;
	final int capacity;
	public LRUCache(int capacity) {
		this.capacity = capacity;
		nodeMap = new HashMap<>(capacity);
		head.next = tail;
		tail.prev = head;
	}

	public int get(int key) {
		if (nodeMap.containsKey(key)) {
			Node node = nodeMap.get(key);
			// move node to head next
			remove(node);
			insertToHeadNext(node);
			return node.value;
		}

		return -1;
	}

	public void put(int key, int value) {
		if (nodeMap.containsKey(key)) {
			Node node = nodeMap.get(key);
			// move node to head next
			remove(node);
			node.value = value;
			insertToHeadNext(node);
		} else {
			if (nodeMap.size() >= capacity) {
				// remove tail prev node
				nodeMap.remove(tail.prev.key);
				remove(tail.prev);
			}

			Node node = new Node(key, value);
			insertToHeadNext(node);
			nodeMap.put(key, node);
		}
	}

	class Node {
		Node prev, next;
		int key, value;

		Node (int k, int v) {
			key = k;
			value = v;
		}
	}

	private void remove(Node node) {
		node.prev.next = node.next;
		node.next.prev = node.prev;
	}

	private void insertToHeadNext(Node node) {
		Node originHeadNext = head.next;
		head.next = node;
		originHeadNext.prev = node;

		node.prev = head;
		node.next = originHeadNext;
	}

}
