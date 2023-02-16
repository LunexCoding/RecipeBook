import unittest
from RecipeBook import Recipe


class TestRecipe(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._recipe = Recipe(
            name="Капустница",
            ingredients={
                2: 300,
                3: 2
            },
            cookingSteps={
                "1": "Белокочанную капусту промываем под холодной водой, чистим лук и морковь.",
                "2": "Капусту нарезаем тонкой соломкой.",
                "3": "Морковь натираем на крупной терке, лук нарезаем кубиками, чеснок либо мелко-мелко нарезаем, либо пропускаем через чесночницу.",
                "4": "Все овощи перекладываем в одну посуду.",
                "5": "Поливаем салат подсолнечным маслом и уксусом, добавляем немножко сахара и соли. Хорошенько перемешиваем."
            },
            description="Едва ли не самый популярный гарнир к котлетам в простых столовых.",
            isFavorite=True,
            rating=12
        )

    def test_recipe(self):
        self.assertEqual([self._recipe.name, self._recipe.rating, self._recipe.isFavorite], ['Капустница', 12, True])


if __name__ == '__main__':
    unittest.main()
