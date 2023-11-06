from _class import Class
from point import Point

data = [
    [321, 140, 218, 29.3, 49.2, 3.7, 17.6, 80, 30],
    [321, 252, 125.5, 27.3, 62.3, 6.2, 21.8, 80, 20],
    [298, 205, 261, 23.3, 60.4, 6.7, 23.3, 70, 26],
    [399, 92, 220.5, 32.4, 55.9, 1.3, 29.2, 120, 51],
    [309, 272, 202.3, 24.6, 73.1, 8.1, 19.7, 80, 30],
    [355, 232, 178.9, 28, 51.5, 6.8, 22.4, 90, 25],
    [206, 160, 72.8, 18.5, 150.5, 31, 11.1, 50, 16],
    [142, 22, 78.2, 10.4, 63.4, 20.4, 9.4, 20, 10],
    [381, 240, 334.6, 27.5, 90, 5.2, 35.7, 80, 46],
    [347, 285, 219, 29.5, 57.6, 5.8, 23.6, 80, 30],
    [338, 311, 236.7, 29.1, 46.7, 3.6, 20.4, 90, 40],
    [115, 25, 94.8, 7.8, 64.3, 22.6, 7, 30, 10],
    [292, 390, 168.5, 24, 77.4, 5.5, 16.8, 70, 20],
    [378, 60, 308.2, 29.4, 56.3, 2.4, 29.4, 110, 45],
    [327, 148, 272.2, 24.7, 65.7, 5.5, 24.7, 80, 44],
    [308, 222, 79.2, 25.6, 63.6, 21.1, 20.5, 80, 13],
    [406, 172, 182.3, 32.5, 76.4, 4.9, 26, 110, 28],
    [292, 276, 132.9, 25.4, 116.4, 32.5, 17.8, 70, 25],
    [344, 192, 87.2, 27.9, 90.1, 36.3, 19.5, 80, 36],
    [367, 256, 264, 28.8, 48.8, 5.7, 23, 90, 30],
    [264, 314, 215.9, 19.5, 103, 36.4, 23.4, 60, 20],
    [342, 336, 211.1, 28.9, 37.1, 27.5, 20.2, 90, 27],
    [401, 112, 259.4, 33.3, 54.9, 1.2, 26.6, 120, 41],
    [314, 238, 209.8, 25.1, 63.7, 6.4, 22.6, 70, 27],
    [314, 353.5, 72.6, 26.3, 51.6, 30.3, 21, 70, 20],
    [80, 41, 146.3, 3.5, 50, 20, 8.3, 10, 11],
    [300, 223, 156.7, 23.4, 53, 4, 21.1, 70, 22],
    [370, 432, 162, 31.2, 83.5, 13.3, 18.7, 100, 25],
    [70, 91, 215.7, 3.4, 42.9, 2.9, 4.1, 13, 14]
]

six_points = [
    [-2, 3],
    [-2, 1],
    [-2, -1],
    [2, -1],
    [2, 1],
    [1, 0]
]


def init(data):
    # transform the data (a simple 2D array) in an array of points
    points = [Point(str(i), 1 / len(data), coord) for i, coord in enumerate(data)]

    # for each point create a class that only contains one point
    classes = [Class(point.label, [point]) for point in points]

    trace = [classes.copy()]  # save a copy of classes at each step
    ward_distances = [0]

    return classes, trace, ward_distances


classes, trace, ward_distances = init(data)

# the program end when there is only one class left
while len(classes) > 1:
    two_nearest, ward_distance = Class.two_nearest(classes)
    new_class = Class.merge(*two_nearest)
    classes.remove(two_nearest[0])
    classes.remove(two_nearest[1])
    classes.append(new_class)
    trace.append(classes.copy())
    ward_distances.append(ward_distance)


def print_2d_array(a):
    for i, elt in enumerate(a):
        print(str(elt[-1]) + " ward_distance = " + str(round(ward_distances[i])))
    print()


print([round(elt) for elt in ward_distances])
print_2d_array(trace)
