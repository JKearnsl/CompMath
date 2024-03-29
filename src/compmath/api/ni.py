from typing import Any

import numpy as np
from PyQt6.QtCore import pyqtSignal

from compmath.api.base import APIBase, urljoin
from compmath.models.graphic import Graphic, PolygonModel, RectModel, GraphModel, PointModel, MeshModel
from compmath.models.ni.base import TableRow
from compmath.utils.data import dicts_to_dataclasses


class NIClient(APIBase):
    lrmCalculated = pyqtSignal(object)
    mrmCalculated = pyqtSignal(object)
    rrmCalculated = pyqtSignal(object)
    sm1Calculated = pyqtSignal(object)
    sm2Calculated = pyqtSignal(object)
    tmCalculated = pyqtSignal(object)
    intermediateCalculated = pyqtSignal(object)

    lrmError = pyqtSignal(str)
    mrmError = pyqtSignal(str)
    rrmError = pyqtSignal(str)
    sm1Error = pyqtSignal(str)
    sm2Error = pyqtSignal(str)
    tmError = pyqtSignal(str)
    intermediateError = pyqtSignal(str)

    def calc_lrm(
            self,
            a: float,
            b: float,
            intervals: int,
            fx: str,
            x_limits: tuple[float, float],
            y_limits: tuple[float, float]
    ) -> None:
        """
        Вычисление методом левых прямоугольников

        :param a: левая граница интервала
        :param b: правая граница интервала
        :param intervals: количество интервалов
        :param fx: функция
        :param x_limits: пределы по оси x
        :param y_limits: пределы по оси y
        :return: список графиков, логов, результатов и названий моделей
        """
        self.post(
            urljoin(self._base_url, "/ni/lrm/calculate"),
            {
                "a": a,
                "b": b,
                "intervals": intervals,
                "fx": fx,
                "x_limits": x_limits,
                "y_limits": y_limits
            },
            [lambda content: self._calculated(self.lrmCalculated, content)],
            [self.lrmError.emit]
        )

    def calc_mrm(
            self,
            a: float,
            b: float,
            intervals: int,
            fx: str,
            x_limits: tuple[float, float],
            y_limits: tuple[float, float]
    ) -> None:
        """
        Вычисление методом средних прямоугольников

        :param a: левая граница интервала
        :param b: правая граница интервала
        :param intervals: количество интервалов
        :param fx: функция
        :param x_limits: пределы по оси x
        :param y_limits: пределы по оси y
        :return: список графиков, логов, результатов и названий моделей
        """
        self.post(
            urljoin(self._base_url, "/ni/mrm/calculate"),
            {
                "a": a,
                "b": b,
                "intervals": intervals,
                "fx": fx,
                "x_limits": x_limits,
                "y_limits": y_limits
            },
            [lambda content: self._calculated(self.mrmCalculated, content)],
            [self.mrmError.emit]
        )

    def calc_rrm(
            self,
            a: float,
            b: float,
            intervals: int,
            fx: str,
            x_limits: tuple[float, float],
            y_limits: tuple[float, float]
    ) -> None:
        """
        Вычисление методом правых прямоугольников

        :param a: левая граница интервала
        :param b: правая граница интервала
        :param intervals: количество интервалов
        :param fx: функция
        :param x_limits: пределы по оси x
        :param y_limits: пределы по оси y
        :return: список графиков, логов, результатов и названий моделей
        """
        self.post(
            urljoin(self._base_url, "/ni/rrm/calculate"),
            {
                "a": a,
                "b": b,
                "intervals": intervals,
                "fx": fx,
                "x_limits": x_limits,
                "y_limits": y_limits
            },
            [lambda content: self._calculated(self.rrmCalculated, content)],
            [self.rrmError.emit]
        )

    def calc_sm1(
            self,
            a: float,
            b: float,
            intervals: int,
            fx: str,
            x_limits: tuple[float, float],
            y_limits: tuple[float, float]
    ) -> None:
        """
        Вычисление методом Симпсона 1

        :param a: левая граница интервала
        :param b: правая граница интервала
        :param intervals: количество интервалов
        :param fx: функция
        :param x_limits: пределы по оси x
        :param y_limits: пределы по оси y
        :return: список графиков, логов, результатов и названий моделей
        """
        self.post(
            urljoin(self._base_url, "/ni/sm1/calculate"),
            {
                "a": a,
                "b": b,
                "intervals": intervals,
                "fx": fx,
                "x_limits": x_limits,
                "y_limits": y_limits
            },
            [lambda content: self._calculated(self.sm1Calculated, content)],
            [self.sm1Error.emit]
        )

    def calc_sm2(
            self,
            a: float,
            b: float,
            intervals: int,
            fx: str,
            x_limits: tuple[float, float],
            y_limits: tuple[float, float]
    ) -> None:
        """
        Вычисление методом Симпсона 2

        :param a: левая граница интервала
        :param b: правая граница интервала
        :param intervals: количество интервалов
        :param fx: функция
        :param x_limits: пределы по оси x
        :param y_limits: пределы по оси y
        :return: список графиков, логов, результатов и названий моделей
        """
        self.post(
            urljoin(self._base_url, "/ni/sm2/calculate"),
            {
                "a": a,
                "b": b,
                "intervals": intervals,
                "fx": fx,
                "x_limits": x_limits,
                "y_limits": y_limits
            },
            [lambda content: self._calculated(self.sm2Calculated, content)],
            [self.sm2Error.emit]
        )

    def calc_tm(
            self,
            a: float,
            b: float,
            intervals: int,
            fx: str,
            x_limits: tuple[float, float],
            y_limits: tuple[float, float]
    ) -> None:
        """
        Вычисление методом трапеций

        :param a: левая граница интервала
        :param b: правая граница интервала
        :param intervals: количество интервалов
        :param fx: функция
        :param x_limits: пределы по оси x
        :param y_limits: пределы по оси y
        :return: список графиков, логов, результатов и названий моделей
        """
        self.post(
            urljoin(self._base_url, "/ni/tm/calculate"),
            {
                "a": a,
                "b": b,
                "intervals": intervals,
                "fx": fx,
                "x_limits": x_limits,
                "y_limits": y_limits
            },
            [lambda content: self._calculated(self.tmCalculated, content)],
            [self.tmError.emit]
        )

    def calc_intermediate(
            self,
            a: float,
            b: float,
            fx: str
    ) -> None:
        """
        Вычисление промежуточных значений

        :param a: левая граница интервала
        :param b: правая граница интервала
        :param fx: функция
        :return: список графиков, логов, результатов и названий моделей
        """
        self.post(
            urljoin(self._base_url, "/ni/intermediate/calculate"),
            {
                "a": a,
                "b": b,
                "fx": fx
            },
            [lambda content: self._calculated_interm(self.intermediateCalculated, content)],
            [self.intermediateError.emit]
        )

    def _calculated_interm(self, signal: pyqtSignal, content: dict[str, Any]):
        plot_items = dicts_to_dataclasses(
            content['graphic_items'],
            [
                MeshModel
            ]
        )
        reference_result = content['reference_result']
        surface_area = content['surface_area']
        volume = content['volume']
        arc_length = content['arc_length']

        graphic = Graphic()
        if plot_items:
            item = plot_items[0]
            graphic.add_mesh(
                vertexes=item.vertexes,
                faces=item.faces,
                shader=item.shader
            )

        signal.emit((graphic, reference_result, surface_area, volume, arc_length))

    def _calculated(self, signal: pyqtSignal, content: dict[str, Any]):
        plot_items = dicts_to_dataclasses(
            content['graphic_items'],
            [
                PolygonModel,
                RectModel,
                GraphModel,
                PointModel
            ]
        )
        table = dicts_to_dataclasses(
            content['table'],
            [
                TableRow
            ]
        )
        result = content['result']
        abs_delta = content['abs_delta']
        relative_delta = content['relative_delta']

        for item in plot_items:
            if isinstance(item, GraphModel):
                if None in item.x_data:
                    for i, coord in enumerate(item.x_data):
                        if coord is None:
                            item.x_data[i] = np.nan
                if None in item.y_data:
                    for i, coord in enumerate(item.y_data):
                        if coord is None:
                            item.y_data[i] = np.nan

        graphic = Graphic()
        graphic.graphs.extend(plot_items)

        signal.emit((graphic, table, result, abs_delta, relative_delta))
