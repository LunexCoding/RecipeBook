class BaseSorting:
    def call(self, recipes):
        return recipes


class SortingByName(BaseSorting):
    def call(self, recipes):
        return dict(sorted(recipes.items(), key=lambda x: x[1].name, reverse=True))


class SortingByRating(BaseSorting):
    def call(self, recipes):
        return dict(sorted(recipes.items(), key=lambda x: x[1].rating, reverse=True))
