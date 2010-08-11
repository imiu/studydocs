/*
 * File: Hailstone.java
 * Name: 
 * Section Leader: 
 * --------------------
 * This file is the starter file for the Hailstone problem.
 */

import acm.program.*;

@SuppressWarnings("serial")
public class Hailstone extends ConsoleProgram {
	public void run() {
		int number = readInt("Enter a number: ");
		
		int counter = 0;
		while (number != 1) {
			if (number % 2 == 0) {
				number /= 2;
				println("is even, so I make half: " + number);
			}
			else {
				number = 3 * number + 1;
				println("is odd, so I make 3n+1: " + number);
			}
			counter++;
		}
		
		println("The process took " + counter + " to reach 1");
	}
}