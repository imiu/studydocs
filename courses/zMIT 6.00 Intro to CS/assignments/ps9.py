# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.
class Triangle(Shape):
    """docstring for Triangle"""
    def __init__(self, base, height):
        self.base = float(base)
        self.height = float(height)
    
    def area(self):
        """Returns approximate area of the triangle"""
        return (0.5 * self.base * self.height)
    
    def __str__(self):
        return 'Triangle with base %0.2f and height %0.2f' %(self.base, self.height)
    
    def __eq__(self, other):
        """Two triangles are equal if their base and height are"""
        return type(other) == Triangle \
        and self.base == other.base \
        and self.height == other.height

#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        self.place = 0
        self.shapes_list = []

    def add_shape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        for shape in self.shapes_list:
            if sh == shape:
                raise ValueError('Duplicate shape')
        self.shapes_list.append(sh)

    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        self.place = 0
        return self
    
    def next(self):
        """docstring for next"""
        if self.place >= len(self.shapes_list):
            raise StopIteration
        self.place += 1
        return self.shapes_list[self.place - 1]

    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        tr = []
        ci = []
        sq = []
        tmp_str = ''
        for shape in self.shapes_list:
            if type(shape) == Square:
                sq.append(shape.__str__())
            elif type(shape) == Circle:
                ci.append(shape.__str__())
            elif type(shape) == Triangle:
                tr.append(shape.__str__())
        if len(tr) > 0:
            tmp_str += '=== Triangles === \n'
            for t in tr:
                tmp_str += t + '\n'
        if len(ci) > 0:
            tmp_str += '=== Circles === \n'
            for c in ci:
                tmp_str += c + '\n'
        if len(sq) > 0:
            tmp_str += '=== Squares === \n'
            for s in sq:
                tmp_str += s + '\n'
        
        return tmp_str

#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    largest = ()
    largest_area = 0
    for shape in shapes:
        if shape.area() > largest_area:
            largest_area = shape.area()
            largest = (shape, )
        elif shape.area() == largest_area:
            largest += (shape, )
    return largest

#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    input_file = open(filename)
    ss = ShapeSet()
    tshape = []
    for line in input_file:
        tshape.append(line.split(','))
    for shape in tshape:
        if shape[0] == 'circle':
            ss.add_shape(Circle(shape[1].strip()))
        elif shape[0] == 'square':
            ss.add_shape(Square(shape[1].strip()))
        elif shape[0] == 'triangle':
            ss.add_shape(Triangle(shape[1].strip(), shape[2].strip()))
    
    return ss

ss = readShapesFromFile("shapes.txt")
print ss