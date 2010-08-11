from numpy.core.numeric import arange
from numpy.core.numeric import array
import random
from matplotlib import pyplot

# pyplot.plot([1, 2, 3, 4])
# pyplot.plot([5, 6, 7, 8])
# pyplot.plot([1, 2, 3, 4], [1, 4, 9, 16])
# pyplot.figure()
# x_axis = array([1, 2, 3, 4])
# test = arange(1, 3)
# y_axis = x_axis ** 3
# pyplot.plot(x_axis, y_axis, 'ro')

pyplot.figure()
vals = []
die_vals = [1, 2, 3, 4, 5, 6]
for i in range(10000):
    vals.append(random.choice(die_vals) + random.choice(die_vals))
print vals
pyplot.hist(vals, bins=11)


pyplot.show()