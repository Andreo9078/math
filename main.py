import matplotlib.pyplot as plt


from points.sets import PointSet, BasePointSet, BasePoint
from points.creators import Point2DCreator

from approximator.approximators import LineFunc2DApproximator, QuadraticFunc2DApproximator, PowerFunc2DApproximator, IndicativeFunc2DApproximator



points_lst = [(2, 3.1), (6, 6.7), (10, 9.5), (14, 11.9), (18, 14), (22, 15.5)]
point_set = PointSet(Point2DCreator())
point_set.points = points_lst

approx_funcs = [LineFunc2DApproximator(point_set),
                   QuadraticFunc2DApproximator(point_set),
                   PowerFunc2DApproximator(point_set),
                   IndicativeFunc2DApproximator(point_set)]


xy = point_set.get_x_y_lists()
plt.scatter(xy[0], xy[1])

for func in approx_funcs:
    print(func.get_approximate_func())
    xy = func.get_xy_lists()
    plt.plot(xy[0], xy[1])

plt.show()