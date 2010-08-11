/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package boardGame;

import java.util.LinkedList;
import java.util.List;

/**
 *
 * @author akudryashov
 */
class Tile {
    private List units;

    public Tile() {
        units = new LinkedList();
    }

    protected void addUnit(Unit unit) {
        units.add(unit);
    }

    protected void removeUnit(Unit unit) {
        units.remove(unit);
    }

    void removeUnits() {
        throw new UnsupportedOperationException("Not yet implemented");
    }

    List getUnits() {
        throw new UnsupportedOperationException("Not yet implemented");
    }

}