import math
import random
from matplotlib import pyplot

class Location(object):
    """docstring for Location"""
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def move(self, xc, yc):
        """docstring for move"""
        return Location(self.x + float(xc), self.y + float(yc))

    def get_coords(self):
        """docstring for get_coords"""
        return self.x, self.y

    def get_dist(self, other):
        """docstring for get_dist"""
        ox, oy = other.get_coords()
        x_dist = self.x - ox
        y_dist = self.y - oy
        return math.sqrt(x_dist ** 2 + y_dist ** 2)


class CompassPt(object):
    """docstring for Compass_pt"""
    possibles = ('N', 'S', 'E', 'W')
    def __init__(self, pt):
        if pt in self.possibles:
            self.pt = pt
        else:
            raise ValueError('in compass_pt __init__')

    def move(self, dist):
        """docstring for move"""
        if self.pt == 'N':
            return (0, dist)
        elif self.pt == 'S':
            return (0, -dist)
        elif self.pt == 'E':
            return (dist, 0)
        elif self.pt == 'W':
            return (-dist, 0)
        else:
            raise ValueError(' in CompassPt.move')


class Field(object):
    """docstring for Field"""
    def __init__(self, drunk, loc):
        super(Field, self).__init__()
        self.drunk = drunk
        self.loc = loc

    def move(self, cp, dist):
        """docstring for move"""
        oldLoc = self.loc
        xc, yc = cp.move(dist)
        self.loc = oldLoc.move(xc, yc)

    def get_loc(self):
        """docstring for get_loc"""
        return self.loc

    def get_drunk(self):
        """docstring for get_drunk"""
        return self.drunk


class Drunk(object):
    """docstring for Drunk"""
    def __init__(self, name):
        self.name = name

    def move(self, field, time = 1):
        """docstring for move"""
        if field.get_drunk() != self:
            raise ValueError('Wrong drunk!')
        for i in range(time):
            pt = CompassPt(random.choice(CompassPt.possibles))
            field.move(pt, 1)

def perform_trial(time, f):
    """docstring for perform_trial"""
    start = f.get_loc()
    distances = [0.0]
    for t in range(1, time + 1):
        f.get_drunk().move(f)
        new_loc = f.get_loc()
        distance = new_loc.get_dist(start)
        distances.append(distance)
    return distances

def first_test():
    """Documentation"""
    d = Drunk('A Drunk')
    for i in range(5):
        f = Field(d, Location(0, 0))
        dist = perform_trial(1, f)
        pyplot.plot(dist)
    pyplot.title('Drunk simulation')
    pyplot.xlabel('Time')
    pyplot.ylabel('Distance')


def perform_simulation(time, num_trials):
    """Documentation"""
    dist_lists = []
    for trial in range(num_trials):
        d = Drunk('Drunk #' + str(trial))
        f = Field(d, Location(0, 0))
        distances = perform_trial(time, f)
        dist_lists.append(distances)
    return dist_lists

def answer_question(max_time, num_trials):
    """Documentation"""
    means = []
    dist_lists = perform_simulation(max_time, num_trials)
    for t in range(max_time + 1):
        tot = 0.0
        for dist_l in dist_lists:
            tot += dist_l[t]
        means.append(tot/len(dist_lists))
    pyplot.figure()
    pyplot.plot(means)
    pyplot.ylabel('distance')
    pyplot.xlabel('time')
    pyplot.title('Average distance for drunk')

answer_question(1000, 1000)
first_test()
pyplot.show()