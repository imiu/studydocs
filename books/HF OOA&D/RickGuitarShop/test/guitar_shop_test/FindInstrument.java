/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package guitar_shop_test;

import guitar_shop.Builder;
import guitar_shop.Instrument;
import guitar_shop.InstrumentSpec;
import guitar_shop.Inventory;
import guitar_shop.Wood;
import guitar_shop.Type;
import guitar_shop.InstrumentType;
import guitar_shop.Style;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

/**
 *
 * @author akudryashov
 */
public class FindInstrument {
    public static void main(String[] args) {
        // Set up Rick's inventory
        Inventory inventory = new Inventory();
        initializeInventory(inventory);

        Map properties = new HashMap();
        properties.put("builder", Builder.GIBSON);
        properties.put("backWood", Wood.MAPLE);
        InstrumentSpec clientSpec = new InstrumentSpec(properties);

        List matchingInstruments = inventory.search(clientSpec);
        if (!matchingInstruments.isEmpty()) {
            for (Iterator i = matchingInstruments.iterator(); i.hasNext(); ) {
                Instrument instrument = (Instrument)i.next();
                InstrumentSpec spec = instrument.getSpec();
                System.out.println("We have a " + spec.getProperty("instrumentType") +
                        " with the following properties: ");
                for (Iterator j = spec.getProperties().keySet().iterator(); j.hasNext(); ) {
                    String propertyName = (String)j.next();
                    if (propertyName.equals("instrumentType"))
                        continue;
                    System.out.println("    " + propertyName + ": " + spec.getProperty(propertyName));
                }
                System.out.println("  You can have this " + spec.getProperty("instrumentType") +
                        " for $" + instrument.getPrice() + "\n===");
            }
        } else {
            System.out.println("Sorry, we have nothing for you");
        }
    }

    private static void initializeInventory(Inventory inventory) {
        Map properties1 = new HashMap();
        properties1.put("instrumentType", InstrumentType.GUITAR);
        properties1.put("builder", Builder.COLLINGS);
        properties1.put("model", "CJ");
        properties1.put("type", Type.ACOUSTIC);
        properties1.put("numStrings", 6);
        properties1.put("topWood", Wood.SITKA);
        inventory.addInstrument("11277", 3999.95, new InstrumentSpec(properties1));

        Map properties2 = new HashMap();
        properties2.put("instrumentType", InstrumentType.GUITAR);
        properties2.put("builder", Builder.MARTIN);
        properties2.put("model", "D-18");
        properties2.put("type", Type.ACOUSTIC);
        properties2.put("numStrings", 6);
        properties2.put("topWood", Wood.MAHOGANY);
        properties2.put("backWood", Wood.ADIRONDACK);
        inventory.addInstrument("122784", 5494.95, new InstrumentSpec(properties2));

        Map properties3 = new HashMap();
        properties3.put("instrumentType", InstrumentType.GUITAR);
        properties3.put("builder", Builder.FENDER);
        properties3.put("model", "Stratocaster");
        properties3.put("type", Type.ELECTRIC);
        properties3.put("numStrings", 6);
        properties3.put("topWood", Wood.ALDER);
        properties3.put("backWood", Wood.ALDER);
        inventory.addInstrument("V95693", 1499.95, new InstrumentSpec(properties3));


        Map properties4 = new HashMap();
        properties4.put("instrumentType", InstrumentType.GUITAR);
        properties4.put("builder", Builder.FENDER);
        properties4.put("model", "Stratocaster");
        properties4.put("type", Type.ELECTRIC);
        properties4.put("numStrings", 6);
        properties4.put("topWood", Wood.ALDER);
        properties4.put("backWood", Wood.ALDER);
        inventory.addInstrument("V9512", 1549.95, new InstrumentSpec(properties4));

        Map properties5 = new HashMap();
        properties5.put("instrumentType", InstrumentType.GUITAR);
        properties5.put("builder", Builder.GIBSON);
        properties5.put("model", "SG'61");
        properties4.put("type", Type.ELECTRIC);
        properties4.put("numStrings", 6);
        properties5.put("topWood", Wood.MAHOGANY);
        properties5.put("backWood", Wood.MAHOGANY);
        inventory.addInstrument("82765501", 1890.95, new InstrumentSpec(properties5));

        Map properties6 = new HashMap();
        properties6.put("instrumentType", InstrumentType.GUITAR);
        properties6.put("builder", Builder.GIBSON);
        properties6.put("model", "Les Paul");
        properties4.put("type", Type.ELECTRIC);
        properties4.put("numStrings", 6);
        properties6.put("topWood", Wood.MAPLE);
        properties6.put("backWood", Wood.MAPLE);
        inventory.addInstrument("70108276", 2295.95, new InstrumentSpec(properties6));

        // Mandolin
        Map properties7 = new HashMap();
        properties7.put("instrumentType", InstrumentType.MANDOLIN);
        properties7.put("builder", Builder.GIBSON);
        properties7.put("model", "F5-G");
        properties7.put("type", Type.ACOUSTIC);
        properties7.put("topWood", Wood.MAPLE);
        properties7.put("backWood", Wood.MAPLE);
        inventory.addInstrument("9019920", 5495.99, new InstrumentSpec(properties7));

        // Banjo
        Map properties8 = new HashMap();
        properties8.put("instrumentType", InstrumentType.BANJO);
        properties8.put("builder", Builder.GIBSON);
        properties8.put("model", "RB-3");
        properties8.put("numStrings", 5);
        properties8.put("type", Type.ACOUSTIC);
        properties8.put("backWood", Wood.MAPLE);
        inventory.addInstrument("8900231", 2945.99, new InstrumentSpec(properties8));
    }
}