from .base import BasePointCreator
from .points import Point2D


class Point2DCreator(BasePointCreator):
    def create_from_dict(self, dc):
        return Point2D(dc["x"], dc["y"])


    def create_from_tuple(self, tup: tuple):
        return Point2D(tup[0], tup[1])