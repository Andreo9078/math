import numpy
from abc import ABC, abstractmethod


from points.sets import BasePointSet


class BasePointsApproximator(ABC):
    @abstractmethod
    def __init__(self, point_set: BasePointSet):
        self.point_set = point_set

    @abstractmethod
    def get_coefs(self):
        pass

    @abstractmethod
    def get_approximate_func(self):
        pass

    @abstractmethod
    def get_aprox_err(self):
        coefs = self.get_coefs()
        s = 0
        for point in self.point_set:
            s += (abs(point.y - self.get_y(point.x, coefs)))/point.y

        return s/len(self.point_set)

    @abstractmethod
    def get_y(self, x, coefs):
        pass

    @abstractmethod
    def get_xy_lists(self):
        coefs = self.get_coefs()
        x, y = self.point_set.get_x_y_lists()
        x_mid = sum(x) / len(x)
        x_lst = numpy.linspace(x[0] - x_mid, x[-1] + x_mid, 100)
        y_lst = self.get_y(x_lst, coefs)

        return [x_lst, y_lst]


class BaseMathFunction(ABC):
    @abstractmethod
    def get_xy_list(self):
        pass