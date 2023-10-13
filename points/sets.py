from .base import BasePointSet, BasePointCreator, BasePoint


class PointSet(BasePointSet):
    def __init__(self,
                 point_creator: BasePointCreator,
                 points: list[BasePoint | dict | tuple] = [],):
        super().__init__(point_creator, points)


    @property
    def points(self):
        return self._points


    @points.setter
    def points(self, points_list: list[BasePoint | dict | tuple],):
        self.set_points(points_list)


    def set_points(self, points_list: list[BasePoint | dict | tuple]):
        if type(points_list) != list:
            raise TypeError

        if len(points_list) == 0:
            self._points = []
        elif type(points_list[0]) == dict:
            self.set_points_from_dicts_list(points_list)
        elif type(points_list[0]) == tuple:
            self.set_points_from_tuples_list(points_list)
        elif isinstance(points_list[0], BasePoint):
            self._points = points_list
        else:
            raise TypeError("points_list may be list, dict or Point types")


    def set_points_from_dicts_list(self, lst: list[dict]):
        for dc in lst:
            self._points.append(self.point_creator.create_from_dict(dc))


    def set_points_from_tuples_list(self, lst: list[tuple]):
        for tup in lst:
            self._points.append(self.point_creator.create_from_tuple(tup))


    def get_x_y_lists(self):
        x = []
        y = []
        for point in self.points:
            x.append(point.x)
            y.append(point.y)

        return [x, y]


    def __iter__(self):
        return iter(self.points)

    def __len__(self):
        return len(self.points)


    def __str__(self):
        res = []
        for point in self.points:
            res.append(str(point))

        return str(res)