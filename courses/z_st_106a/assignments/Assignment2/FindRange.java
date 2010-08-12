/*
 * File: FindRange.java
 * Name: 
 * Section Leader: 
 * --------------------
 * This file is the starter file for the FindRange problem.
 */

import acm.program.*;

@SuppressWarnings("serial")
public class FindRange extends ConsoleProgram {
	private static final int SENTINEL = 0;
	public void run() {
		println("This program finds the largest and smallest numbers.");
		int a;
		int smallest = 0;
		int largest = 0;
		int counter = 0;
		while(true) {
			a = readInt("? ");
			if (a == SENTINEL) {
				break;
			}
			if (a > largest) {
				largest = a;
			}
			if (a < smallest) {
				smallest = a;
			}
			counter++;
		}
		if (counter == 0) {
			println("You entered stop as first number. Exiting.");
		}
		else {
			println("smallest: " + smallest);
			println("largest: " + largest);
		}
	}
}