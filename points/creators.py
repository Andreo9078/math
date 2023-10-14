from .base import BasePointCreator
from .points import Point2D


class Point2DCreator(BasePointCreator):
    def create_from_dict(self, dc):
        return Point2D(float(dc["x"]), float(dc["y"]))


    def create_from_tuple(self, tup: tuple):
        return Point2D(float(tup[0]), float(tup[1]))