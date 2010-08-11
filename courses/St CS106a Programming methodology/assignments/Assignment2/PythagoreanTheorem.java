/*
 * File: PythagoreanTheorem.java
 * Name: 
 * Section Leader: 
 * -----------------------------
 * This file is the starter file for the PythagoreanTheorem problem.
 */

import acm.program.*;

@SuppressWarnings("serial")
public class PythagoreanTheorem extends ConsoleProgram {
	public void run() {
		double a;
		double b;
		double c;
		println("Enter values to compute Pythagorean theorem.");
		
		a = readDouble("a: ");
		b = readDouble("b: ");
		
		c = Math.sqrt(a*a + b*b);
		println("c = " + c);
	}
}