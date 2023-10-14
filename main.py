import matplotlib.pyplot as plt


from points.sets import PointSet, BasePointSet, BasePoint
from points.creators import Point2DCreator

from approximator.approximators import LineFunc2DApproximator, QuadraticFunc2DApproximator, PowerFunc2DApproximator, IndicativeFunc2DApproximator



points_lst = [(3, 26), (5, 76), (7, 150), (9, 240), (11, 360), (13, 500)]
point_set = PointSet(Point2DCreator())
point_set.points = points_lst

approx_funcs = [LineFunc2DApproximator(point_set),
                   QuadraticFunc2DApproximator(point_set),
                   PowerFunc2DApproximator(point_set),
                   IndicativeFunc2DApproximator(point_set)]


xy = point_set.get_x_y_lists()
plt.scatter(xy[0], xy[1])

for func in approx_funcs:
    xy = func.get_xy_lists()
    label = func.get_approximate_func()
    plt.plot(xy[0], xy[1], label=label)

plt.legend()
plt.tight_layout()
plt.show()