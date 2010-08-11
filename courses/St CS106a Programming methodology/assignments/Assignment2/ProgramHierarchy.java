/*
 * File: ProgramHierarchy.java
 * Name: 
 * Section Leader: 
 * ---------------------------
 * This file is the starter file for the ProgramHierarchy problem.
 */

import acm.graphics.*;
import acm.program.*;

@SuppressWarnings("serial")
public class ProgramHierarchy extends GraphicsProgram {
	private static final int BLOCK_WIDTH = 160;
	private static final int BLOCK_HEIGHT = 50;
	private static final int BLOCK_WHITESPACE = 20;
	
	public void run() {
		int scrWidth = getWidth();
		int scrHeight = getHeight();
		int x = scrWidth / 2;
		int y = scrHeight / 2;
		
		x -= BLOCK_WIDTH / 2;
		y -= BLOCK_HEIGHT + BLOCK_HEIGHT / 2;
		GRect pBlock = new GRect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT);
		add(pBlock);
		
		GLabel pLabel = new GLabel("Program");
		double pLWidth = pLabel.getWidth();
		double pLHeight = pLabel.getAscent();
		pLabel.setLocation(x + BLOCK_WIDTH / 2 - pLWidth / 2, y + BLOCK_HEIGHT / 2 + pLHeight / 2);
		add(pLabel);
		
		x = scrWidth / 2 - BLOCK_WIDTH / 2 - BLOCK_WIDTH - BLOCK_WHITESPACE;
		y = scrHeight / 2 + BLOCK_HEIGHT / 2;
		int xLine = scrWidth / 2;
		int yLine = scrHeight /2 - BLOCK_HEIGHT / 2;
		for (int numRect = 0; numRect < 3; numRect++) {
			GRect curRect = new GRect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT);
			add(curRect);
			
			GLine curLine = new GLine(xLine, yLine, x + BLOCK_WIDTH / 2, y);
			add(curLine);
			
			String labelText = "";
			switch(numRect) {
			case 0:
				labelText = "GraphicsProgram";
				break;
			case 1:
				labelText = "ConsoleProgram";
				break;
			case 2:
				labelText = "DialogProgram";
				break;
			}
			
			GLabel curLabel = new GLabel(labelText);
			double curLWidth = curLabel.getWidth();
			double curLHeight = curLabel.getAscent();
			curLabel.setLocation(x + BLOCK_WIDTH / 2 - curLWidth / 2, y + BLOCK_HEIGHT / 2 + curLHeight / 2);
			add(curLabel);

			x += BLOCK_WIDTH + BLOCK_WHITESPACE;
		}
	}
}

