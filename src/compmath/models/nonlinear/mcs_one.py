from compmath.models.nonlinear.base import BaseNoNLinearModel, TableRow
from compmath.models.nonlinear.graphic import Graphic
from compmath.utils.func import make_callable, line_between_points, derivative


class MCSOneModel(BaseNoNLinearModel):

    def __init__(self):
        super().__init__()
        self._title = "Метод секущих (Одно шаговый)"
        self._description = """
        """
        self._fx = "x**3 - 2*x - 5"
        self._interval = (2, 3)
        self._eps = 0.001

    def calc(self) -> None:
        """
        Метод секущих одно шаговый

        :return:
        """
        self.graphics.clear()
        self.table.clear()

        function = make_callable(self.fx)
        a, b = self.interval

        if function(a) * function(b) > 0:
            self.raise_error("На данном интервале нет корней")
            return

        if derivative(derivative(function))(a) * function(a) > 0:
            c = b
            x = a
        else:
            c = a
            x = b

        n = 0
        while True:
            x -= (function(x) * (x - c)) / (function(x) - function(c))
            n += 1

            graphic = Graphic(x_limits=self.x_limits)
            graphic.add_graph(function)
            graphic.add_graph(line_between_points(a, function(a), b, function(b)), x_limits=(a, b))
            graphic.add_point(x, function(x), color="red")
            graphic.add_point(a, function(a), color="yellow")
            graphic.add_point(b, function(b), color="yellow")
            self.graphics.append(graphic)

            self.table.append(
                TableRow(
                    iter_num=n,
                    x=x,
                    fx=function(x),
                    a=a,
                    fa=function(a),
                    b=b,
                    fb=function(b),
                    distance=abs(a - b)
                )
            )

            if abs(function(x)) <= self.eps or n >= self.iters_limit:
                break

        self.result = x
        self.iters = n
        self.was_calculated()