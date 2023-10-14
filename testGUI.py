import sys
from PySide6 import QtCore, QtWidgets, QtGui
import matplotlib.pyplot as plt

from points.sets import PointSet, BasePointSet, BasePoint
from points.creators import Point2DCreator

from approximator.approximators import LineFunc2DApproximator, QuadraticFunc2DApproximator, PowerFunc2DApproximator, IndicativeFunc2DApproximator


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(445, 500)
        self.setWindowTitle("Function Approximator")
        self.poins_count = 1

        self.table = QtWidgets.QTableWidget()
        self.table.setRowCount(self.poins_count)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["x", "y"])

        self.line_fuck_checkbox = QtWidgets.QCheckBox("Line Function Approximate")
        self.quad_funk_checkbox = QtWidgets.QCheckBox("Quadratic Function Approximate")
        self.power_funk_checkbox = QtWidgets.QCheckBox("Power Function Approximate")
        self.indicative_funk_checkbox = QtWidgets.QCheckBox("Indicative Function Approximate")

        self.add_button = QtWidgets.QPushButton("Add Point")
        self.del_button = QtWidgets.QPushButton("Delete Point")
        self.get_button = QtWidgets.QPushButton("Create Plot")

        self.buttons_layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.Direction.RightToLeft)
        self.buttons_layout.addWidget(self.get_button)
        self.buttons_layout.addWidget(self.del_button)
        self.buttons_layout.addWidget(self.add_button)

        self.checkbox_lt = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.Direction.TopToBottom)
        self.checkbox_lt.addWidget(self.indicative_funk_checkbox)
        self.checkbox_lt.addWidget(self.power_funk_checkbox)
        self.checkbox_lt.addWidget(self.quad_funk_checkbox)
        self.checkbox_lt.addWidget(self.line_fuck_checkbox)

        self.table_checkbox_lt = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.Direction.RightToLeft)
        self.table_checkbox_lt.addLayout(self.checkbox_lt)
        self.table_checkbox_lt.addWidget(self.table)


        self.layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.Direction.BottomToTop, self)
        self.layout.addLayout(self.buttons_layout)
        self.layout.addLayout(self.table_checkbox_lt)

        self.add_button.clicked.connect(self.magic)
        self.del_button.clicked.connect(self.magic2)
        self.get_button.clicked.connect(self.graf)

    @QtCore.Slot()
    def magic(self):
        self.poins_count += 1
        self.table.setRowCount(self.poins_count)

    @QtCore.Slot()
    def magic2(self):
        if self.poins_count > 0:
            self.poins_count -= 1
            self.table.setRowCount(self.poins_count)

    @QtCore.Slot()
    def graf(self):
        plt.close('all')
        rows = self.table.rowCount()
        cols = self.table.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                point = self.table.item(row, col)
                if point:
                    tmp.append(point.text())
                else:
                    continue
            if tmp:
                data.append(tmp)

        point_set = PointSet(Point2DCreator())
        point_set.points = data

        approx_funcs = []
        if self.line_fuck_checkbox.isChecked():
            approx_funcs.append(LineFunc2DApproximator(point_set))
        if self.quad_funk_checkbox.isChecked():
            approx_funcs.append(QuadraticFunc2DApproximator(point_set))
        if self.power_funk_checkbox.isChecked():
            approx_funcs.append(PowerFunc2DApproximator(point_set))
        if self.indicative_funk_checkbox.isChecked():
            approx_funcs.append(IndicativeFunc2DApproximator(point_set))


        xy = point_set.get_x_y_lists()
        plt.scatter(xy[0], xy[1])

        if approx_funcs:
            for func in approx_funcs:
                xy = func.get_xy_lists()
                label = func.get_approximate_func()
                plt.plot(xy[0], xy[1], label=label)


        plt.legend()
        plt.tight_layout()
        plt.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec())