/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package dogs_door;

/**
 *
 * @author akudryashov
 */
public class Bark {
    private String sound;

    public Bark(String sound) {
        this.sound = sound;
    }

    public String getSound() {
        return sound;
    }

    public boolean equals(Object bark) {
        if (bark instanceof Bark) {
            Bark otherBark = (Bark)bark;
            if (this.sound.equalsIgnoreCase(otherBark.sound)) {
                return true;
            }
        }
        return false;
    }

    @Override
    public String toString() {
        return sound;
    }
}