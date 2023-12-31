import numpy
from math import e


from .base import BasePointsApproximator
from points.base import BasePointSet


class LineFuncRegCoefsMixin:
    def get_main_d(self):
        return (len(self.point_set) * self.x2_sum - self.x_sum ** 2)

    def get_a_d(self):
        return (len(self.point_set) * self.xy_sum - self.x_sum * self.y_sum)

    def get_b_d(self):
        return (self.x2_sum * self.y_sum - self.x_sum * self.xy_sum)

    def get_coefs(self):
        d = self.get_main_d()
        a = self.get_a_d() / d
        b = self.get_b_d() / d

        return (a, b)


class LineFunc2DApproximator(BasePointsApproximator, LineFuncRegCoefsMixin):
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
        return LineFuncRegCoefsMixin.get_coefs(self)

    def get_y(self, x, coefs):
        return coefs[0] * x + coefs[1]

    def get_xy_lists(self):
        return super().get_xy_lists()

    def get_aprox_err(self):
        return super().get_aprox_err()

    def get_approximate_func(self):
        coefs = self.get_coefs()

        return f"y = {round(coefs[0], 3)} * x + {round(coefs[1], 3)}"


class PowerFunc2DApproximator(BasePointsApproximator, LineFuncRegCoefsMixin):
    def __init__(self, point_set: BasePointSet):
        super().__init__(point_set)

        self.x_sum = 0
        self.y_sum = 0
        self.xy_sum = 0
        self.x2_sum = 0

        self._culc_sums()

    def _culc_sums(self):
        for point in self.point_set:
            self.x_sum += numpy.log(point.x)
            self.y_sum += numpy.log(point.y)
            self.x2_sum += numpy.log(point.x) ** 2
            self.xy_sum += numpy.log(point.x) * numpy.log(point.y)

    def get_coefs(self):
        b, a = LineFuncRegCoefsMixin.get_coefs(self)

        return (e ** a, b)

    def get_y(self, x, coefs):
        return coefs[0] * (x ** coefs[1])

    def get_xy_lists(self):
        return super().get_xy_lists()

    def get_aprox_err(self):
        return super().get_aprox_err()

    def get_approximate_func(self):
        coefs = self.get_coefs()

        return f"y = {round(coefs[0], 3)} * x ^ {round(coefs[1], 3)}"


class IndicativeFunc2DApproximator(BasePointsApproximator, LineFuncRegCoefsMixin):
    def __init__(self, point_set: BasePointSet):
        super().__init__(point_set)

        self.x_sum = 0
        self.y_sum = 0
        self.xy_sum = 0
        self.x2_sum = 0

        self._culc_sums()

    def _culc_sums(self):
        for point in self.point_set:
            self.y_sum += numpy.log(point.y)
            self.xy_sum += point.x * numpy.log(point.y)
            self.x_sum += point.x
            self.x2_sum += point.x ** 2

    def get_coefs(self):
        b, a = LineFuncRegCoefsMixin.get_coefs(self)

        return (e ** a, b)

    def get_y(self, x, coefs):

        return coefs[0] * (e ** (coefs[1] * x))

    def get_xy_lists(self):
        return super().get_xy_lists()

    def get_aprox_err(self):
        return super().get_aprox_err()

    def get_approximate_func(self):
        coefs = self.get_coefs()

        return f"y = {round(coefs[0], 3)} * {round(e ** coefs[1], 3)} ^ x"


class QuadraticFunc2DApproximator(BasePointsApproximator):
    def __init__(self, point_set: BasePointSet):
        super().__init__(point_set)
        self.n = len(point_set)
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

    def get_main_d(self):
        matrix = numpy.array([[self.x4, self.x3, self.x2],
                              [self.x3, self.x2, self.x],
                              [self.x2, self.x, self.n]])
        return numpy.linalg.det(matrix)

    def get_a_d(self):
        matrix = numpy.array([[self.x2y, self.x3, self.x2],
                              [self.xy, self.x2, self.x],
                              [self.y, self.x, self.n]])
        return numpy.linalg.det(matrix)

    def get_b_d(self):
        matrix = numpy.array([[self.x4, self.x2y, self.x2],
                              [self.x3, self.xy, self.x],
                              [self.x2, self.y, self.n]])
        return numpy.linalg.det(matrix)

    def get_c_d(self):
        matrix = numpy.array([[self.x4, self.x3, self.x2y],
                              [self.x3, self.x2, self.xy],
                              [self.x2, self.x, self.y]])
        return numpy.linalg.det(matrix)

    def get_coefs(self):
        d = self.get_main_d()
        d1 = self.get_a_d()
        d2 = self.get_b_d()
        d3 = self.get_c_d()

        return (d1/d, d2/d, d3/d)

    def get_y(self, x, coefs):
        return coefs[0] * (x ** 2) + coefs[1] * x + coefs[2]

    def get_xy_lists(self):
        return super().get_xy_lists()

    def get_aprox_err(self):
        return super().get_aprox_err()

    def get_approximate_func(self):
        coefs = self.get_coefs()

        return f"y = {round(coefs[0], 3)} * x^2 + {round(coefs[1], 3)} * x + {round(coefs[2], 3)}"
