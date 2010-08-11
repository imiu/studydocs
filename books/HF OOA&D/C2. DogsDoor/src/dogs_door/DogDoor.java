/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package dogs_door;

import java.util.LinkedList;
import java.util.List;
import java.util.Timer;
import java.util.TimerTask;
/**
 *
 * @author akudryashov
 */
public class DogDoor {
    private boolean open;
    private List allowedBark;

    public DogDoor() {
        this.allowedBark = new LinkedList();
        this.open = false;
    }

    public void open() {
        System.out.println("The dog door opens.");
        open = true;

        final Timer timer = new Timer();
        timer.schedule(new TimerTask() {
            public void run() {
                close();
                timer.cancel();
            }
        }, 5000);
    }

    public void close() {
        System.out.println("The dog door closes");
        open = false;
    }

    public boolean isOpen() {
        return open;
    }

    public void addAllowedBark(Bark bark) {
        this.allowedBark.add(bark);
    }

    public List getAllowedBarks() {
        return allowedBark;
    }
}