import numpy
from math import e

from .base import BasePointsApproximator
from points.base import BasePointSet


class LineFunc2DApproximator(BasePointsApproximator):
    def __init__(self, point_set: BasePointSet):
        super().__init__(point_set)
        self.x_sum = 0
        self.y_sum = 0
        self.xy_sum = 0
        self.x2_sum = 0

        self._culc_sums()


    def _culc_sums(self):
        for point in self.point_set:
            self.x_sum += point.x
            self.y_sum += point.y
            self.xy_sum += point.x * point.y
            self.x2_sum += point.x ** 2


    def get_coefs(self):
        point_set_len = len(self.point_set)

        a = (self.x_sum * self.y_sum - point_set_len * self.xy_sum)\
           /(self.x_sum ** 2 - point_set_len * self.x2_sum)
        b = (self.x_sum * self.xy_sum - self.x2_sum * self.y_sum)\
           /(self.x_sum ** 2 - point_set_len * self.x2_sum)

        return (a, b)


    def get_xy_lists(self):
        coefs = self.get_coefs()
        x, y = self.point_set.get_x_y_lists()
        x_lst = numpy.linspace(x[0], x[-1], 100)
        y_lst = coefs[0] * x_lst + coefs[1]

        return [x_lst, y_lst]

    def get_approximate_func(self):
        coefs = self.get_coefs()

        return f"y = {round(coefs[0], 3)} * x + {round(coefs[1], 3)}"


class PowerFunc2DApproximator(BasePointsApproximator):
    def __init__(self, point_set: BasePointSet):
        super().__init__(point_set)

        self.lnx = 0
        self.lny = 0
        self.ln2x = 0
        self.lnxlny = 0

        self._culc_sums()


    def _culc_sums(self):
        for point in self.point_set:
            self.lnx += numpy.log(point.x)
            self.lny += numpy.log(point.y)
            self.ln2x += numpy.log(point.x) ** 2
            self.lnxlny += numpy.log(point.x) * numpy.log(point.y)

    def get_coefs(self):
        point_set_len = len(self.point_set)
        matrix = numpy.array([[point_set_len, self.lnx],
                              [self.lnx, self.ln2x]])
        d = numpy.linalg.det(matrix)

        matrix = numpy.array([[self.lny, self.lnx],
                              [self.lnxlny, self.ln2x]])
        d1 = numpy.linalg.det(matrix)

        matrix = numpy.array([[point_set_len, self.lny],
                              [self.lnx, self.lnxlny]])
        d2 = numpy.linalg.det(matrix)

        return (e ** (d1/d), d2/d)


    def get_xy_lists(self):
        coefs = self.get_coefs()
        x, y = self.point_set.get_x_y_lists()
        x_lst = numpy.linspace(x[0], x[-1], 100)
        y_lst = coefs[0] * (x_lst ** coefs[1])

        return [x_lst, y_lst]


    def get_approximate_func(self):
        coefs = self.get_coefs()

        return f"y = {round(coefs[0], 3)} * x ^ {round(coefs[1], 3)}"


class QuadraticFunc2DApproximator(BasePointsApproximator):
    def __init__(self, point_set: BasePointSet):
        super().__init__(point_set)

        self.x, self.y = 0, 0
        self.xy, self.x2 = 0, 0
        self.x3, self.x4 = 0, 0
        self.x2y = 0

        self._culc_sums()


    def _culc_sums(self):
        for point in self.point_set:
            self.x += point.x
            self.y += point.y
            self.xy += point.x * point.y
            self.x2y += point.x ** 2 * point.y
            self.x2 += point.x ** 2
            self.x3 += point.x ** 3
            self.x4 += point.x ** 4


    def get_coefs(self):
        point_set_len = len(self.point_set)
        matrix = numpy.array([[self.x4, self.x3, self.x2],
                              [self.x3, self.x2, self.x],
                              [self.x2, self.x, point_set_len]])
        d = numpy.linalg.det(matrix)

        matrix = numpy.array([[self.x2y, self.x3, self.x2],
                              [self.xy, self.x2, self.x],
                              [self.y, self.x, point_set_len]])
        d1 = numpy.linalg.det(matrix)

        matrix = numpy.array([[self.x4, self.x2y, self.x2],
                              [self.x3, self.xy, self.x],
                              [self.x2, self.y, point_set_len]])
        d2 = numpy.linalg.det(matrix)

        matrix = numpy.array([[self.x4, self.x3, self.x2y],
                              [self.x3, self.x2, self.xy],
                              [self.x2, self.x, self.y]])
        d3 = numpy.linalg.det(matrix)

        return (round(d1/d, 3), round(d2/d, 3), round(d3/d, 3))


    def get_xy_lists(self):
        coefs = self.get_coefs()
        x, y = self.point_set.get_x_y_lists()
        x_lst = numpy.linspace(x[0], x[-1], 100)
        y_lst = coefs[0] * (x_lst ** 2) + coefs[1] * x_lst + coefs[2]

        return [x_lst, y_lst]


    def get_approximate_func(self):
        coefs = self.get_coefs()

        return f"y = {coefs[0]} * x^2 + {coefs[1]} * x + {coefs[2]}"


class IndicativeFunc2DApproximator(BasePointsApproximator):
    def __init__(self, point_set: BasePointSet):
        super().__init__(point_set)

        self.lny = 0
        self.xlny = 0
        self.x = 0
        self.x2 = 0

        self._culc_sums()


    def _culc_sums(self):
        for point in self.point_set:
            self.lny += numpy.log(point.y)
            self.xlny += point.x * numpy.log(point.y)
            self.x += point.x
            self.x2 += point.x ** 2


    def get_coefs(self):
        point_set_len = len(self.point_set)
        b = e ** ((point_set_len * self.xlny - self.x * self.lny)\
                 /(point_set_len * self.x2 - (self.x ** 2)))

        a = e ** (self.lny / point_set_len - (numpy.log(b) / point_set_len) * self.x)

        return (a, b)


    def get_xy_lists(self):
        coefs = self.get_coefs()
        x, y = self.point_set.get_x_y_lists()
        x_lst = numpy.linspace(x[0], x[-1], 100)
        y_lst = coefs[0] * coefs[1] ** x_lst

        return [x_lst, y_lst]


    def get_approximate_func(self):
        coefs = self.get_coefs()

        return f"y = {round(coefs[0], 3)} * {round(coefs[1], 2)} ^ x"