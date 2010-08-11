/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package puzzle;

/**
 *
 * @author akudryashov
 */
public class Jet extends Airplane {
    private static final int MULTIPLIER = 2;

    public Jet() {
        super();
    }

    public void setSpeed(int speed) {
        super.setSpeed(speed * MULTIPLIER);
    }

    public void accelerate() {
        super.setSpeed(getSpeed() * 2);
    }
}