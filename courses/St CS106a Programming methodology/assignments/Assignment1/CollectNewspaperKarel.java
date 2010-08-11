/*
 * File: CollectNewspaperKarel.java
 * --------------------------------
 * At present, the CollectNewspaperKarel subclass does nothing.
 * Your job in the assignment is to add the necessary code to
 * instruct Karel to walk to the door of its house, pick up the
 * newspaper (represented by a beeper, of course), and then return
 * to its initial position in the upper left corner of the house.
 */

import stanford.karel.*;

public class CollectNewspaperKarel extends SuperKarel {

	public void run() {
		findNewspaper();
		getNewspaper();
		goBack();
	}	
	
	private void findNewspaper() {
		moveForward();
		turnRight();
		while(leftIsBlocked()) {
			move();
		}
		turnLeft();
	}
	
	private void getNewspaper() {
		while(noBeepersPresent()) {
			move();
		}
		pickBeeper();
	}
	
	private void goBack() {
		while(notFacingWest()) {
			turnLeft();
		}
		moveForward();
		turnRight();
		moveForward();
		turnRight();
	}
	
	private void moveForward() {
		while(frontIsClear()) {
			move();
		}
	}

}