from logger import logger


log = logger.getLogger(__name__)


class Ingredient:

    def __init__(self, name=None, amount=None, measure=None):
        self._name = name
        self._amount = amount
        self._measure = measure
        log.debug(f'Ингредиент {self._name} был создан')

    @property
    def name(self):
        return self._name

    @property
    def amount(self):
        return self._amount

    @property
    def measure(self):
        return self._measure
