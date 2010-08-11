# Problem Set 11: Simulating robots
# Name:
# Collaborators:
# Time:

import math
import ps11_visualize
from matplotlib import pyplot
import random

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).

        x: a real number indicating the x-coordinate
        y: a real number indicating the y-coordinate
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: integer representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)


# === Problems 1 and 2

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.tiles = {}
        for i in range(self.width):
            for j in range(self.height):
                self.tiles[(i, j)] = False

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        self.tiles[int(pos.getX()), int(pos.getY())] = True
        
    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.tiles[m, n]

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return len(self.tiles)
    
    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """

        return len(filter((lambda k: self.tiles[k] == True), self.tiles))
    
    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        x = random.choice(range(self.width))
        y = random.choice(range(self.height))
        return Position(x, y)

    def isPositionInRoom(self, pos):
        """
        Return True if POS is inside the room.

        pos: a Position object.
        returns: True if POS is in the room, False otherwise.
        """
        if pos.getX() > 0 and pos.getY() > 0 and \
           pos.getX() < self.width and pos.getY() < self.height:
            return True
        else:
            return False


class BaseRobot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in
    the room.  The robot also has a fixed speed.

    Subclasses of BaseRobot should provide movement strategies by
    implementing updatePositionAndClean(), which simulates a single
    time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified
        room. The robot initially has a random direction d and a
        random position p in the room.

        The direction d is an integer satisfying 0 <= d < 360; it
        specifies an angle in degrees.

        p is a Position object giving the robot's position.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.p = self.room.getRandomPosition()
        self.d = random.choice(range(360))

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.p
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.d
    
    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.p = position
    
    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.d = direction


class Robot(BaseRobot):
    """
    A Robot is a BaseRobot with the standard movement strategy.

    At each time-step, a Robot attempts to move in its current
    direction; when it hits a wall, it chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """

        while 1:
            tmp_p = self.p.getNewPosition(self.d, self.speed)
            if self.room.isPositionInRoom(tmp_p):
                break
            else:
                self.d = (random.choice(range(360)))
        self.p = tmp_p
        self.room.cleanTileAtPosition(self.p)

# === Problem 3
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type, visualize):
    """
    Runs NUM_TRIALS trials of the simulation and returns a list of
    lists, one per trial. The list for a trial has an element for each
    timestep of that trial, the value of which is the percentage of
    the room that is clean after that timestep. Each trial stops when
    MIN_COVERAGE of the room is clean.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE,
    each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    Visualization is turned on when boolean VISUALIZE is set to True.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    visualize: a boolean (True to turn on visualization)
    """
    result = []
    # anim = ps11_visualize.RobotVisualization(num_robots, width, height)
    for i in range(0, num_trials):
#        anim = ps11_visualize.RobotVisualization(num_robots, width, height)
        # Initialize room and robots
        room = RectangularRoom(width, height)
        robots = []
        for j in range(0, num_robots):
            robots.append(robot_type(room, speed))
        # Run the simulation
        room_coverrage = 0
        trial_result = []
        while room_coverrage < min_coverage:
            for r in robots:
                r.updatePositionAndClean()
            room_coverrage = (float(room.getNumCleanedTiles()) / room.getNumTiles())
            trial_result.append(room_coverrage)
#            anim.update(room, robots)
        result.append(trial_result)
#        anim.done()
    return result

# === Provided function
def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.

    Lists shorter than the longest list are padded with their final
    value to be the same length.
    """
    # Find length of longest list
    longest = 0
    for lst in list_of_lists:
        if len(lst) > longest:
           longest = len(lst)
    # Get totals
    tots = [0]*(longest)
    for lst in list_of_lists:
        for i in range(longest):
            if i < len(lst):
                tots[i] += lst[i]
            else:
                tots[i] += lst[-1]
    # Convert tots to an array to make averaging across each index easier
    tots = pylab.array(tots)
    # Compute means
    means = tots/float(len(list_of_lists))
    return means

def avg_list_len(list):
    """Documentation"""
    total_lenght = 0.0
    for l in list:
        total_lenght += len(l)
    return total_lenght / len(list)

# === Problem 4
def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on room size.
    """
    num_robots = 1
    num_trials = 5
    speed = 1
    min_coverage = 0.75
    x_values = []
    y_values = []
    for i in range(5, 30, 5):
        y_values.append(avg_list_len(runSimulation(num_robots, speed, i, i,
                        min_coverage, num_trials, Robot, False)))
        x_values.append(i)
    pyplot.plot(x_values, y_values)
    pyplot.xlabel('Room size')
    pyplot.ylabel('Time')
    pyplot.title('Time by room size')
    pyplot.show()

# showPlot1()

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    room_width = 25
    room_height = 25
    num_trials = 5
    speed = 1
    min_coverage = 0.75
    x_values = []
    y_values = []
    for i in range(1, 11):
        y_values.append(avg_list_len(runSimulation(i, speed, room_width, room_height,
                        min_coverage, num_trials, Robot, False)))
        x_values.append(i)
    print y_values
    pyplot.plot(x_values, y_values)
    pyplot.xlabel('Robot count')
    pyplot.ylabel('Time')
    pyplot.title('Time by robot count')
    pyplot.show()

#showPlot2()

def showPlot3():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    room_width = [20, 25, 40, 50, 80, 100]
    room_height = [20, 16, 10, 8, 5, 4]
    num_trials = 20
    speed = 1
    min_coverage = 0.75
    x_values = []
    y_values = []
    for i in range(6):
        print i
        tw = room_width[i]
        th = room_height[i]
        y_values.append(avg_list_len(runSimulation(2, speed, tw, th,
                        min_coverage, num_trials, Robot, False)))
        x_values.append(i)
    print y_values
    pyplot.plot(x_values, y_values)
    pyplot.xlabel('Room dims')
    pyplot.ylabel('Time')
    pyplot.title('Time by room shape')
    pyplot.show()

# showPlot3()

def showPlot4():
    """
    Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
    """
    room_width = 25
    room_height = 25
    num_trials = 1
    speed = 1
    for r in range(1, 6):
        x_values = []
        y_values = []
        for i in range(1, 101):
            cleanage_per = float(i) / 100
            y_values.append(avg_list_len(runSimulation(r, speed, room_width,
                            room_height, cleanage_per, num_trials, Robot, False)))
            x_values.append(i)
        pyplot.figure(1)
        pyplot.plot(x_values, y_values, label = str(r) + ' robots')
    pyplot.xlabel('% cleanage')
    pyplot.ylabel('Time')
    pyplot.title('Time by % cleaned and robots')
    pyplot.show()

#showPlot4()
# === Problem 5

class RandomWalkRobot(BaseRobot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement
    strategy: it chooses a new direction at random after each
    time-step.
    """
    def updatePositionAndClean(self):
        while 1:
            self.d = (random.choice(range(360)))
            tmp_p = self.p.getNewPosition(self.d, self.speed)
            if self.room.isPositionInRoom(tmp_p):
                break
            else:
                self.d = (random.choice(range(360)))
        self.p = tmp_p
        self.room.cleanTileAtPosition(self.p)

#runSimulation(1, 1, 10, 10, 1, 1, RandomWalkRobot, True)
# === Problem 6

def showPlot5():
    """
    Produces a plot comparing the two robot strategies.
    """
    num_robots = 5
    num_trials = 10
    speed = 1
    min_coverage = 0.75
    x_values = []
    y_values = []
    for i in range(5, 30, 5):
        y_values.append(avg_list_len(runSimulation(num_robots, speed, i, i,
                        min_coverage, num_trials, Robot, False)))
        x_values.append(i)
    pyplot.figure(1)
    pyplot.plot(x_values, y_values, label='Logic')

    x_values = []
    y_values = []
    for i in range(5, 30, 5):
        y_values.append(avg_list_len(runSimulation(num_robots, speed, i, i,
                        min_coverage, num_trials, RandomWalkRobot, False)))
        x_values.append(i)
    pyplot.figure(1)
    pyplot.plot(x_values, y_values, label='Random')
    pyplot.xlabel('Room size')
    pyplot.ylabel('Time')
    pyplot.title('Time by room size')
    pyplot.legend()
    pyplot.show()

showPlot5()