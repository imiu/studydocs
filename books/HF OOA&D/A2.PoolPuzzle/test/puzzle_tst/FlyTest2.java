/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package puzzle_tst;
import puzzle.*;

/**
 *
 * @author akudryashov
 */
public class FlyTest2 {
    public static void main(String[] args) {
        Jet jet1 = new Jet();
        jet1.speed = 212;
        System.out.println(jet1.speed);

        Jet jet2 = new Jet();
        jet2.setSpeed(212);
        System.out.println(jet2.getSpeed());

    }
}
