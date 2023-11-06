import math
from typing import List, Tuple


class Point:
    # constructor
    def __init__(self, label: str, weight: float, coord: List):
        self.label = label
        self.coord = coord
        self.dimension = len(coord)
        self.weight = weight

    # cf doc
    def __str__(self):
        return self.label + ": " + str(self.coord) + "  (" + "{:.2f}".format(self.weight) + ")"

    # find the euclidian distance between two points
    @staticmethod
    def distance_euclidienne(p1: 'Point', p2: 'Point') -> float:
        if p1.dimension != p2.dimension:
            print("ERROR : the two points don't have the same dimension [Point.distance_euclidienne()]")
            return False

        sum = 0
        for i in range(p1.dimension):
            delta = abs(p1.coord[i] - p2.coord[i])
            sum += delta ** 2
        return math.sqrt(sum)

    # useless
    @staticmethod
    def dist_min(points: List['Point']) -> Tuple['Point', 'Point']:
        p1 = points[0]
        p2 = points[1]
        min_distance = Point.distance_euclidienne(points[0], points[1])
        for i in range(1, len(points)):
            for j in range(i + 1, len(points)):
                dist = Point.distance_euclidienne(points[i], points[j])
                if dist < min_distance:
                    min_distance = dist
                    p1 = points[i]
                    p2 = points[j]
        return p1, p2
