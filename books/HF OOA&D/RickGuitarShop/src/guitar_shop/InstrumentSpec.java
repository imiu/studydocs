/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package guitar_shop;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

/**
 *
 * @author akudryashov
 */
public class InstrumentSpec {
    private Map properties;

    public InstrumentSpec(Map properties) {
        if (properties == null) {
            this.properties = new HashMap();
        } else {
            this.properties = new HashMap(properties);
        }
        this.properties = properties;
    }

    public Object getProperty(String propertyName) {
        return properties.get(propertyName);
    }

    public Map getProperties() {
        return this.properties;
    }

    public boolean equals(InstrumentSpec otherSpec) {
        for (Iterator i = otherSpec.getProperties().keySet().iterator(); i.hasNext(); ) {
            String propertyName = (String)i.next();
            if(!properties.get(propertyName).equals(otherSpec.getProperty(propertyName))) {
                return false;
            }
        }
        return true;
    }
}