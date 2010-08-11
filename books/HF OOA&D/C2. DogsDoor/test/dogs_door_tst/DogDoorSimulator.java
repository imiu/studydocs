/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package dogs_door_tst;

import dogs_door.Bark;
import dogs_door.BarkRecognizer;
import dogs_door.DogDoor;
import dogs_door.Remote;

/**
 *
 * @author akudryashov
 */
public class DogDoorSimulator {
    @SuppressWarnings("static-access")
    public static void main(String[] args) {
        DogDoor door = new DogDoor();
        door.addAllowedBark(new Bark("rowlf"));
        door.addAllowedBark(new Bark("rooowlf"));
        door.addAllowedBark(new Bark("rawlf"));
        door.addAllowedBark(new Bark("woof"));
        BarkRecognizer recognizer = new BarkRecognizer(door);
        Remote remote = new Remote(door);
        
        // Simulate the hardware hearing a bark
        System.out.println("Bruce starts barking...");
        recognizer.recognize(new Bark("rowlf"));

        System.out.println("\nBruce has gone outside...");

        try {
            Thread.currentThread().sleep(10000);
        } catch (InterruptedException e) { }

        System.out.println("\nBruce's all done...");
        System.out.println("...but he's stuck outside");

        // Simulate another dog
        Bark smallDogBark = new Bark("yip");
        System.out.println("\nA small dog starts barking...");
        recognizer.recognize(smallDogBark);

        try {
            Thread.currentThread().sleep(5000);
        } catch (InterruptedException e) { }

        // Simulate our dog
        System.out.println("\nBruce starts barking...");
        recognizer.recognize(new Bark("rooowlf"));

        System.out.println("\nBruce's back inside");
    }
}