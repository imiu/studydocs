/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package guitar_shop;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

/**
 *
 * @author akudryashov
 */
public class Inventory {
    private List inventory;

    public Inventory() {
        inventory = new LinkedList();
    }

    public void addInstrument(String serialNumber, double price, InstrumentSpec spec) {
        Instrument instrument = new Instrument(serialNumber, price, (InstrumentSpec)spec);
        inventory.add(instrument);
    }

    public Instrument get(String serialNumber) {
        for (Iterator i = inventory.iterator(); i.hasNext();) {
            Instrument instrument = (Instrument)i.next();
            if (instrument.getSerialNumber().equals(serialNumber)) {
                return instrument;
            }
        }
        return null;
    }

    public List search(InstrumentSpec searchSpec) {
        List matchingInstruments = new LinkedList();
        for (Iterator i = inventory.iterator(); i.hasNext(); ) {
            Instrument instrument = (Instrument)i.next();
            // Ignore serial number since that's unique
            // Ignore price since that's unique
            if (instrument.getSpec().equals(searchSpec))
                matchingInstruments.add(instrument);
        }
        return matchingInstruments;
    }
}