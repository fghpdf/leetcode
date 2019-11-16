package com.fghpdf.Concurrency;

/**
 * @author fghpdf
 * @date 2019/11/16
 **/
public class VolatileVisibility {
	// volatile
	private static volatile boolean initFlag = false;

	public static void main(String[] args) throws InterruptedException {
		new Thread(() -> {
			System.out.println("waiting data ...");
			while (!initFlag) {

			}
			System.out.println("done");
		}).start();

		Thread.sleep(2000);

		new Thread(() -> {
			System.out.println("change data");
			initFlag = true;
			System.out.println("changed");
		}).start();
	}
}
