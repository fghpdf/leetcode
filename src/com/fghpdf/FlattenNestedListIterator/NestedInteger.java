package com.fghpdf.FlattenNestedListIterator;

import java.util.List;

/**
 * @author fghpdf
 * @date 2020/1/4
 **/
public interface NestedInteger {
	/**
	 *
	 * @return true if this NestedInteger holds a single integer, rather than a nested list.
	 */
	boolean isInteger();

	/**
	 *
	 * @return the single integer that this NestedInteger holds, if it holds a single integer
	 * Return null if this NestedInteger holds a nested list
	 */
	Integer getInteger();

	/**
	 *
	 * @return the nested list that this NestedInteger holds, if it holds a nested list
	 * Return null if this NestedInteger holds a single integer
	 */
	List<NestedInteger> getList();
}
