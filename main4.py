import matplotlib.pyplot as plt
from Point import Point
import math


# Основна функція
def main():
    points = []
    print("Enter X,Y values for 4 points:")
    for i in range(4):
        try:
            tmp_x = float(input("X{}: ".format(i+1)))
            tmp_y = float(input("Y{}: ".format(i + 1)))
        except ValueError:
            print("Wrong values for points!")
            exit()
        else:
            tmp_point = Point(tmp_x, tmp_y)
            print(Point.get_count())
            points.append(tmp_point)
    show_points(points)
    task1(points)
    show_points(points)
    save_points(points)


def task1(list_of4_points):

    point_1 = list_of4_points[0]
    point_2 = list_of4_points[1]
    point_3 = list_of4_points[2]
    point_4 = list_of4_points[3]


    length = math.sqrt(math.pow(point_4.get_x() - point_3.get_x(), 2) + math.pow(point_4.get_y() - point_3.get_y(), 2))
    point_1.shift(0.0, 41.0)
    print("Length = {}".format(length))

def show_points(list_of_points):
    # work with plot
    x = [point.get_x() for point in list_of_points]
    y = [point.get_y() for point in list_of_points]
    plt.plot(x, y, 'ro')
    plt.grid()
    plt.show()
def save_points(list_of_points):
    with open("output.txt", "w") as f:
        for num, point in enumerate(list_of_points):  # 0: point1, 1: point2, 2: point3, 3: point4
            #f.write(f"{num+1}: {point.get_x()}; {point.get_y()}\n")
            f.write(f"({num+1}) {point.get_x()}:{point.get_y()}\n")


if __name__ == '__main__':
    main()