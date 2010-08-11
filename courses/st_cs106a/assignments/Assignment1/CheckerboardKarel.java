/*
 * File: CheckerboardKarel.java
 * ----------------------------
 * When you finish writing it, the CheckerboardKarel class should draw
 * a checkerboard using beepers, as described in Assignment 1.  You
 * should make sure that your program works for all of the sample
 * worlds supplied in the starter folder.
 */

import stanford.karel.*;

public class CheckerboardKarel extends SuperKarel {

	public void run() {
		int cnt = 1;
		while(northIsClear()) {
			turnEast();
			if (cnt % 2 == 0) {
				fillEvenRow();
				moveWest();
				stepNorth();
				turnEast();
			}
			else {
				fillOddRow();
				moveWest();
				stepNorth();
				turnEast();
			}
			cnt++;
		}
		turnEast();
		if (cnt % 2 == 0) {
			fillEvenRow();
			moveWest();
		}
		else {
			fillOddRow();
			moveWest();
		}
	}
	
	private void fillOddRow() {
		int cnt = 1;
		while(frontIsClear()) {
			if (cnt % 2 == 0) {
				moveIfPossible();
			}
			else {
				putBeeper();
				moveIfPossible();
			}
			cnt++;
		}
		if ((cnt % 2 != 0) && noBeepersPresent()) {
			putBeeper();
		}
	}
	
	private void fillEvenRow() {
		int cnt = 1;
		while(frontIsClear()) {
			if (cnt % 2 != 0) {
				moveIfPossible();
			}
			else {
				putBeeper();
				moveIfPossible();
			}
			cnt++;
		}
		if ((cnt % 2 == 0) && noBeepersPresent()) {
			putBeeper();
		}
	}
	
	private void turnWest() {
		while(notFacingWest()) {
			turnLeft();
		}
	}
	
	private void turnEast() {
		while(notFacingEast()) {
			turnLeft();
		}
	}
	
	private void turnNorth() {
		while(notFacingNorth()) {
			turnLeft();
		}
	}
	
	private boolean westIsClear() {
		turnWest();
		if(frontIsClear()) {
			return true;
		}
		else {
			return false;
		}
	}
	
	private boolean northIsClear() {
		turnNorth();
		if(frontIsClear()) {
			return true;
		}
		else {
			return false;
		}
	}
	
	private void moveWest() {
		while(westIsClear()) {
			move();
		}
	}
	
	private void stepNorth() {
		turnNorth();
		move();
	}
	
	private void moveIfPossible() {
		if (frontIsClear()) {
			move();
		}
	}
}