/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package guitar_shop;

/**
 *
 * @author akudryashov
 */
public enum Type {
    ACOUSTIC, ELECTRIC;

    @Override
    public String toString() {
        switch (this) {
            case ACOUSTIC: return "acoustic";
            case ELECTRIC: return "electric";
            default: return "";
        }
    }
}