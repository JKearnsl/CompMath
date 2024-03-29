from compmath.api.slat import SLATClient
from compmath.models.slat.base import BaseSLATModel, TableRow


class SIModel(BaseSLATModel):

    def __init__(self, api_client: SLATClient):
        super().__init__()
        self._api_client = api_client
        self._api_client.simCalculated.connect(self.process_values)
        self._api_client.simError.connect(self.validation_error)

        self._title = "Метод простых итераций"
        self._description = ""

        self.matrix: list[list[int | float]] = [
            [2.39, -0.48, 1.08, 4.13],
            [0.54, 1.82, 0.73, 2.42],
            [0.32, -0.65, 1.11, -0.47]
        ] # S1 + S2 ; S2 - S3

    def calc(self):
        self._api_client.calc_sim(
            self.a(),
            self.b(),
            self.eps,
            self.iters_limit,
            self.x0
        )

    def process_values(self, content: list[tuple[list[str], list[TableRow], str]]):
        self.results = content
        self.notify_observers()
