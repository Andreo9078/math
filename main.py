import matplotlib.pyplot as plt


from points.sets import PointSet, BasePointSet, BasePoint
from points.creators import Point2DCreator

from approximator.approximators import LineFunc2DApproximator, QuadraticFunc2DApproximator, PowerFunc2DApproximator, IndicativeFunc2DApproximator


points_lst = [(2, 3.1), (6, 6.7), (10, 9.5), (14, 11.9), (18, 14), (22, 15.5)]
point_set = PointSet(Point2DCreator())
point_set.points = points_lst

approx_funcs = [(LineFunc2DApproximator(point_set), "Line Function"),
                (QuadraticFunc2DApproximator(point_set), "Quadratic Function"),
                (PowerFunc2DApproximator(point_set), "Power Function"),
                (IndicativeFunc2DApproximator(point_set), "Indicative Function")]


xy = point_set.get_x_y_lists()
plt.scatter(xy[0], xy[1])

for func, func_name in approx_funcs:
    xy = func.get_xy_lists()
    label = func.get_approximate_func()
    coefs = ""
    dets = f"d: {round(func.get_main_d(), 3)}  " \
           f"d1: {round(func.get_a_d(), 3)}  " \
           f"d2: {round(func.get_b_d(), 3)}  "
    try:
        sums = f"x_sum: {round(func.x_sum, 3)}  " \
               f"y_sum: {round(func.y_sum, 3)}  " \
               f"x2_sum: {round(func.x2_sum, 3)}  " \
               f"xy_sum: {round(func.xy_sum, 3)}"
    except:
        sums = f"x_sum: {round(func.x, 3)}  " \
               f"y_sum: {round(func.y, 3)}  " \
               f"xy_sum: {round(func.xy, 3)}  " \
               f"x2y_sum: {round(func.x2y, 3)}  " \
               f"x2_sum: {round(func.x2, 3)}  " \
               f"x3_sum: {round(func.x3, 3)}  " \
               f"x4_sum: {round(func.x4, 3)} "

    for coef_name, coef in zip(["a", "b", "c"], func.get_coefs()):
        coefs += f"{coef_name}: {round(coef, 3)}  "

    try:
        dets += f"d3: {round(func.get_c_d(), 3)}"
    except:
        pass

    print(f"\n{func_name}\n"
          f"{sums}\n"
          f"{dets}\n"
          f"{coefs}\n"
          f"err = {round(func.get_aprox_err() * 100, 3)} %"
          )
    plt.plot(xy[0], xy[1], label=label)

plt.legend()
plt.tight_layout()
plt.show()