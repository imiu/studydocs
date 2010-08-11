/*
 * File: MidpointFindingKarel.java
 * -------------------------------
 * When you finish writing it, the MidpointFindingKarel class should
 * leave a beeper on the corner closest to the center of 1st Street
 * (or either of the two central corners if 1st Street has an even
 * number of corners).  Karel can put down additional beepers as it
 * looks for the midpoint, but must pick them up again before it
 * stops.  The world may be of any size, but you are allowed to
 * assume that it is at least as tall as it is wide.
 */

import stanford.karel.*;

public class MidpointFindingKarel extends SuperKarel {

	public void run() {
		int cnt = 0;
		while(frontIsClear()) {
			cnt++;
			move();
		}
		turnWest();
		for (int i = 1; i <= cnt/2; i++) {
			move();
		}
		putBeeper();
	}
	
	private void turnWest() {
		while(notFacingWest()) {
			turnLeft();
		}
	}

}