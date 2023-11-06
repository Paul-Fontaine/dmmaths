from point import Point
from typing import List, Tuple


class Class:
    # constructor
    def __init__(self, label: str, points: List[Point]):
        self.label = label
        self.points = points
        self.dimension = points[0].dimension if points else 0
        self.weight = self.find_weight()
        self.g = self.find_center_of_gravity()

    # cf doc
    def __str__(self) -> str:
        return self.label + ": gravity point = " + str([round(x) for x in self.g.coord]) + ",  weight = " + "{:.2f}".format(self.weight)

    # cf doc
    def __add__(self, other):
        return Class.merge(self, other)

    # the weight of a class is equal to the sum of the weight of all points
    def find_weight(self) -> float:
        return sum([p.weight for p in self.points])  # cf doc comprehension list

    # the center of gravity of a class is the average point from all points
    def find_center_of_gravity(self) -> Point:
        point_g = Point("G(" + self.label + ")", self.weight, [None] * self.dimension)
        for i in range(self.dimension):
            axe = [p.coord[i] for p in self.points]  # projection on each axes
            point_g.coord[i] = sum(axe) / len(axe)  # average for each axes
        return point_g

    # simply add a point to the class and recalculate the weight and the center of gravity
    def add_point(self, point: Point):
        self.points.append(point)
        self.weight = self.find_weight()
        self.g = self.find_center_of_gravity()

    # the ward distance between two classes
    @staticmethod
    def ward_distance(c1: 'Class', c2: 'Class') -> float:
        if c1.dimension != c2.dimension:
            print("ERROR : the two classes don't have the same dimension [Class.ward_distance()]")
            return False

        w = c1.weight * c2.weight / (c1.weight + c2.weight)
        d = Point.distance_euclidienne(c1.g, c2.g) ** 2
        return w * d

    # return the two nearest classes from a list of classes
    @staticmethod
    def two_nearest(classes: List['Class']) -> Tuple[Tuple['Class', 'Class'], float]:
        # init with the first two classes
        c1 = classes[0]
        c2 = classes[1]
        min_distance = Class.ward_distance(c1, c2)
        for i in range(0, len(classes) - 1):
            for j in range(i + 1, len(classes)):
                dist = Class.ward_distance(classes[i], classes[j])
                if dist < min_distance:
                    min_distance = dist
                    c1 = classes[i]
                    c2 = classes[j]
        return (c1, c2), min_distance

    # useless
    def nearest_class(self, classes: List['Class']) -> 'Class':
        min_distance = float('inf')
        for other_class in classes:
            dist = Class.ward_distance(self, other_class)
            if dist < min_distance:
                min_distance = dist
                nearest_class = other_class
        return nearest_class

    # merge two classes
    @staticmethod
    def merge(c1: 'Class', c2: 'Class') -> 'Class':
        if c1.dimension != c2.dimension:
            print("ERROR : the two classes don't have the same dimension [Class.merge()]")
            return False

        new_class = Class(c1.label + '+' + c2.label, [])
        new_class.points = c1.points + c2.points
        new_class.dimension = c1.dimension
        new_class.weight = c1.weight + c2.weight
        new_class.g = new_class.find_center_of_gravity()  # recalculate the center of gravity with the new points
        return new_class
