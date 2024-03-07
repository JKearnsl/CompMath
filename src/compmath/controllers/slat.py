from compmath.api.factory import APIFactory
from compmath.views.slat import SLATView
from compmath.views.widgets import WidgetsFactory


class SLATController:

    def __init__(self, model, widgets_factory: 'WidgetsFactory', api_factory: APIFactory, parent):
        self.model = model
        self.widgets_factory = widgets_factory
        self.api_factory = api_factory
        self.view = SLATView(self, self.model, widgets_factory, parent)

        self.view.show()
        self.view.model_loaded()

