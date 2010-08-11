/*
 * File: Target.java
 * Name: 
 * Section Leader: 
 * -----------------
 * This file is the starter file for the Target problem.
 */

import acm.graphics.*;
import acm.program.*;
import java.awt.*;

@SuppressWarnings("serial")
public class Target extends GraphicsProgram {	
	public void run() {
		int centerX = getWidth() / 2;
		int centerY = getHeight() / 2;

		int x = centerX - 72/2;
		int y = centerY - 72/2;
		Color color = Color.red;
		add(getFilledCircle(x, y, 72, color));

		x = centerX - 46/2;
		y = centerY - 46/2;
		color = Color.white;
		add(getFilledCircle(x, y, 46, color));

		x = centerX - 22/2;
		y = centerY - 22/2;
		color = Color.red;
		add(getFilledCircle(x, y, 22, color));
	}
	
	private GOval getFilledCircle(int x, int y, float r, Color color) {
		GOval circle = new GOval(x, y, r, r);
		circle.setFillColor(color);
		circle.setColor(color);
		circle.setFilled(true);
		
		return circle;
	}
}