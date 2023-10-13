from .base import BasePoint


class Point2D(BasePoint):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def as_dict(self):
        return {"x": self.x,
                "y": self.y}

    def as_tuple(self):
        return (self.x, self.y)

    def __str__(self):
        return f"(X: {self.x}, Y: {self.y})"
