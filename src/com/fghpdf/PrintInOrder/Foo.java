package com.fghpdf.PrintInOrder;

import java.util.concurrent.Semaphore;

/**
 * @author fghpdf
 * @date 2019/12/7
 * https://leetcode.com/problems/print-in-order/
 * semaphore the params is the initial number of permits available.
 * so first run will release one resource.
 * and two will run when it get one resource.
 **/
public class Foo {
	private Semaphore run2, run3;

	public Foo() {
		run2 = new Semaphore(0);
		run3 = new Semaphore(0);
	}

	public void first(Runnable printFirst) throws InterruptedException {

		// printFirst.run() outputs "first". Do not change or remove this line.
		printFirst.run();
		run2.release();
	}

	public void second(Runnable printSecond) throws InterruptedException {
		run2.acquire();
		// printSecond.run() outputs "second". Do not change or remove this line.
		printSecond.run();
		run3.release();
	}

	public void third(Runnable printThird) throws InterruptedException {
		run3.acquire();
		// printThird.run() outputs "third". Do not change or remove this line.
		printThird.run();
	}
}

