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
    def get_xy_lists(self):
        pass


class BaseMathFunction(ABC):
    @abstractmethod
    def get_xy_list(self):
        pass