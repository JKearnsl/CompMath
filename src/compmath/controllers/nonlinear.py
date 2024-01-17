from compmath.views.nonlinear import NoNLinearView
from compmath.views.widgets import WidgetsFactory


class NoNLinearController:

    def __init__(self, model, widgets_factory: 'WidgetsFactory', parent):
        self.model = model
        self.widgets_factory = widgets_factory
        self.view = NoNLinearView(self, self.model, widgets_factory, parent)

        self.view.show()
        self.view.model_loaded()

