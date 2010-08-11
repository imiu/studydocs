/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package guitar_shop;

/**
 *
 * @author akudryashov
 */
public enum InstrumentType {
    GUITAR, BANJO, MANDOLIN, DOBRO, FIDDLE, BASS;

    @Override
    public String toString() {
        switch (this) {
            case GUITAR: return "guitar";
            case BANJO: return "banjo";
            case MANDOLIN: return "mandolin";
            case DOBRO: return "dobro";
            case FIDDLE: return "fiddle";
            case BASS: return "bass";
            default: return "Unspecified";
        }
    }
}