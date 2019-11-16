package com.fghpdf.Concurrency;

/**
 * @author fghpdf
 * @date 2019/11/16
 **/
public class VolatileAtomic {
	private static volatile int num = 0;

	private static void atom() {
		num++;
	}

	public static void main(String[] args) throws InterruptedException {
		Thread[] threads = new Thread[10];

		for (int i = 0; i < threads.length; i++) {
			threads[i] = new Thread(() -> {
				for (int j = 0; j < 1000; j++) {
					atom();
				}
			});
			threads[i].start();
		}

		for (Thread t : threads) {
			t.join();
		}

		System.out.println(num);
	}
}
