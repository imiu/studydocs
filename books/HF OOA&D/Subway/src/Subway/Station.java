/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package Subway;

/**
 *
 * @author akudryashov
 */
public class Station {
    private String name;

    public Station(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Station) {
            Station otherStation = (Station)obj;
            if (otherStation.getName().equalsIgnoreCase(name)) {
                return true;
            }
        }

        return false;
    }

    @Override
    public int hashCode() {
        return name.toLowerCase().hashCode();
    }
}