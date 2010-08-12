/*
 * File: Pyramid.java
 * Name: 
 * Section Leader: 
 * ------------------
 * This file is the starter file for the Pyramid problem.
 * It includes definitions of the constants that match the
 * sample run in the assignment, but you should make sure
 * that changing these values causes the generated display
 * to change accordingly.
 */

import acm.graphics.*;
import acm.program.*;

@SuppressWarnings("serial")
public class Pyramid extends GraphicsProgram {

/** Width of each brick in pixels */
	private static final int BRICK_WIDTH = 30;

/** Width of each brick in pixels */
	private static final int BRICK_HEIGHT = 12;

/** Number of bricks in the base of the pyramid */
	private static final int BRICKS_IN_BASE = 19;
	
	public void run() {
		int scrWidth = getWidth();
		int scrHeight = getHeight();
		int pyrWidth = BRICK_WIDTH * BRICKS_IN_BASE;
		int pyrStart = (scrWidth - pyrWidth) / 2;
		int x = pyrStart;
		int y = scrHeight;
		for (int bricksInLine = BRICKS_IN_BASE; bricksInLine > 0; bricksInLine--) {
			x = pyrStart + (pyrWidth - BRICK_WIDTH * bricksInLine) / 2;
			y -= BRICK_HEIGHT;
			for (int curBricks = bricksInLine; curBricks > 0; curBricks--) {
				GRect curBrick = new GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT);
				add(curBrick);
				x += BRICK_WIDTH;
			}
		}
	}
}

