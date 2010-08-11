/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package sumuduck;

/**
 *
 * @author akudryashov
 */
public class MuteQuack implements QuackBehavior {
    public void quack() {
        System.out.println("<< Silence >>");
    }
}