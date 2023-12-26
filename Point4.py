class Point:


    __x: float = 0.0
    __y: float = 0.0
    __point_count: int = 0

    def __init__(self, x: float, y: float):
        self.set_x(x)
        self.set_y(y)
        Point.__point_count += 1

    def __del__(self):
        print("Point has been deleted")
        Point.__point_count -= 1

    def get_x(self):
        return self.__x

    def set_x(self, value):
        if value <= 100 and value >= -100:
            self.__x = value
        else:
            self.__x = 0.0

    def set_y(self, value):
        if value <= 100 and value >= -100:
            self.__y = value
        else:
            self.__y = 0.0

    def get_y(self):
        return self.__y

    def shift(self, x_shift: float, y_shift: float):
        self.set_x(self.get_x() + x_shift)
        self.set_y(self.get_y() + y_shift)

    @staticmethod
    def get_count():
        return Point.__point_count