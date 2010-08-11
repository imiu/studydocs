/*
 * File: StoneMasonKarel.java
 * --------------------------
 * The StoneMasonKarel subclass as it appears here does nothing.
 * When you finish writing it, it should solve the "repair the quad"
 * problem from Assignment 1.  In addition to editing the program,
 * you should be sure to edit this comment so that it no longer
 * indicates that the program does nothing.
 */

import stanford.karel.*;

public class StoneMasonKarel extends SuperKarel {
	public void run() {
		turnLeft();
		repairColumn();
		while(eastIsClear()) {
			findNextColumn();
			repairColumn();
		}	
	}
	
	private boolean eastIsClear() {
		while(notFacingEast()) {
			turnLeft();
		}
		if(frontIsClear()) {
			return true;
		}
		else {
			return false;
		}
	}
	
	public void findNextColumn() {
		for(int i = 0; i < 4; i++) {
			move();
		}
		if(leftIsBlocked()) {
			turnRight();
		}
		else {
			turnLeft();
		}
	}
	
	private void repairColumn() {
		while(frontIsClear()) {
			if(beepersPresent()) {
				move();
			}
			else {
				putBeeper();
				move();
			}
		}
	}
}
