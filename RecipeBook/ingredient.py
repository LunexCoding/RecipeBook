from logger import logger


log = logger.getLogger(__name__)


class Ingredient:

    def __init__(self, name=None, measure=None):
        self._name = name
        self._measure = measure

    @property
    def name(self):
        return self._name

    @property
    def measure(self):
        return self._measure
