package com.fghpdf.FlattenNestedListIterator;

import java.util.Iterator;
import java.util.List;
import java.util.Stack;

/**
 * @author fghpdf
 * @date 2020/1/4
 * @link https://leetcode.com/problems/flatten-nested-list-iterator/
 * use stack to handle hasNext
 **/
public class NestedIterator implements Iterator<Integer> {
	Stack<NestedInteger> stack = new Stack<>();
	public NestedIterator(List<NestedInteger> nestedList) {
		for (int i = nestedList.size() - 1; i >= 0; i--) {
			stack.push(nestedList.get(i));
		}
	}

	@Override
	public Integer next() {
		return stack.pop().getInteger();
	}

	@Override
	public boolean hasNext() {
		while (!stack.empty()) {
			NestedInteger current = stack.peek();
			if (current.isInteger()) {
				return true;
			}
			stack.pop();
			for (int i = current.getList().size() - 1; i >= 0; i--) {
				stack.push(current.getList().get(i));
			}
		}
		return false;
	}
}

