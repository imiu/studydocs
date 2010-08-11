/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package boardGame;

/**
 *
 * @author akudryashov
 */
public class UnitTester {
    public void testType(Unit unit, String type, String expectedOutputType) {
        System.out.println("\nTesting setting/getting the type property.");
        unit.setType(type);
        String outputType = unit.getType();
        if (expectedOutputType.equals(outputType)) {
            System.out.println("Test passed");
        } else {
            System.out.println("Test falied: " + outputType + " did not match " + expectedOutputType);
        }
    }

    public void testUnitSpecificProperty(Unit unit, String propertyName, Object inputValue, Object expectedOutputValue) {
        System.out.println("\nTesting setting/getting a unit-specific property.");
        unit.setProperty(propertyName, inputValue);
        Object outputValue = unit.getProperty(propertyName);
        if (expectedOutputValue.equals(outputValue)) {
            System.out.println("Test passed");
        } else {
            System.out.println("Test failed: " + outputValue + " did not match " + expectedOutputValue);
        }
    }

    public void testChangeProperty(Unit unit, String propertyName, Object inputValue, Object expectedOutputValue) {
        System.out.println("\nTesting changing an existing property's value");
        unit.setProperty(propertyName, inputValue);
        Object outputValue = unit.getProperty(propertyName);
        if (expectedOutputValue.equals(outputValue)) {
            System.out.println("Test passed");
        } else {
            System.out.println("Test failed: " + outputValue + " did not match " + expectedOutputValue);
        }
    }

    public void testNonExistingProperty(Unit unit, String propertyName) {
        System.out.println("\nTesting getting a non-existent property's value");

        try {
            Object outputValue = unit.getProperty(propertyName);
        } catch (RuntimeException e) {
            System.out.println("Test passed");
            return;
        }
        System.out.println("Test failed");
    }

    public void testGetIdProperty(Unit unit, Object expectedOutputValue) {
        System.out.println("\nTesting get the id property");
        Object outputValue = unit.getId();
        if (expectedOutputValue.equals(outputValue)) {
            System.out.println("Test passed");
        } else {
            System.out.println("Test failed with value of " + outputValue);
        }
    }

    public static void main(String args[]) {
        UnitTester tester = new UnitTester();
        Unit unit = new Unit(1000);
        tester.testType(unit, "infantry", "infantry");
        tester.testUnitSpecificProperty(unit, "hitPoints", new Integer(25), new Integer(25));
        tester.testChangeProperty(unit, "hitPoints", new Integer(15), new Integer(15));
        tester.testNonExistingProperty(unit, "strength");
        tester.testGetIdProperty(unit, new Integer(1000));
    }
}