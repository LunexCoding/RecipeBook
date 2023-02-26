class _BaseSorting:
    def call(self, recipes):
        return recipes


class _SortingByName(_BaseSorting):
    def call(self, recipes):
        return dict(sorted(recipes.items(), key=lambda x: x[1].name, reverse=True))


class _SortingByRating(_BaseSorting):
    def call(self, recipes):
        return dict(sorted(recipes.items(), key=lambda x: x[1].rating, reverse=True))


baseSorting = _BaseSorting()
sortingByName = _SortingByName()
sortingByRating = _SortingByRating()
