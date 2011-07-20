name = 'Zed A. Shaw'
age = 35
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall. That's %d in cm" % (height, height * 2.54)
print "He's {0} pounds heavy. That's {1} in kg".format(weight, weight * 0.4535)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d" % (age, height, weight, age + height + weight)
