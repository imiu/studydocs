/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package guitar_shop;

/**
 *
 * @author akudryashov
 */
public class Instrument {
    private String serialNumber;
    private double price;
    private InstrumentSpec spec;

    public Instrument (String serialNumber, double price, InstrumentSpec spec) {
        this.serialNumber = serialNumber;
        this.price = price;
        this.spec = spec;
    }

    public String getSerialNumber() {
        return serialNumber;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }

    public InstrumentSpec getSpec() {
        return spec;
    }
}