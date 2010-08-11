/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package Subway;

import java.io.File;

/**
 *
 * @author akudryashov
 */
public class LoadTester {
    public static void main(String[] args) {
        try {
            SubwayLoader loader = new SubwayLoader();
            Subway objectville = loader.loadFromFile(new File("/Users/akudryashov/Desktop/sbw.txt"));
            System.out.println("Testing stations");
            if (objectville.hasStation("DRY Drive") &&
                objectville.hasStation("Weather-O-Rama, Inc.") &&
                objectville.hasStation("Boards 'R' Us")) {
                System.out.println("... station test passed successfully.");
            } else {
                System.out.println("... station test FAILED");
                System.exit(-1);
            }

            System.out.println("\nTesting connections...");
            if (objectville.hasConnection("DRY Drive", "Head First Theater", "Meyer Line") &&
                objectville.hasConnection("Weather-O-Rama, Inc.", "XHTML Expressway", "Wirfs-Brock Line") &&
                objectville.hasConnection("Head First Theater", "Infinite Circle", "Rumbaugh Line")) {
                System.out.println("... connections test passed successfully");
            } else {
                System.out.println("... connecitons test FAILED");
                System.exit(-1);
            }
        } catch (Exception e) {
            e.printStackTrace(System.out);
        }
    }
}