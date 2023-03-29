from helpers.logger import logger


_log = logger.getLogger(__name__)


class Ingredient:
    def __init__(self, name="Name", measure="Measure"):
        self._name = name
        self._measure = measure
        _log.debug(f"Ингредиент <{self._name}> создан")

    @property
    def name(self):
        return self._name

    @property
    def measure(self):
        return self._measure
