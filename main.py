from logger import logger
from RecipeBook import g_RecipeBook, Ingredient, Recipe
from ingredientsDB import g_ingredientsDB
from storage import g_storage


def main():
    # Тестирование функционала
    # Ingredients, ingredientsDB
    g_ingredientsDB.loadIngredients()
    ingredientNames = ['Белокочанная капуста', 'мясо', 'Морковь', 'Луковица', 'Чеснок',
                       'Подсолнечное масло', 'Уксус', 'Сахар', 'Соль', 'пиво']
    ingredientMeasures = ['гр', 'кг', 'шт', 'шт', 'зубчика', 'ст. ложек', 'Чайная ложка', 'Чайная ложка', 'щепотка', 'л']
    for name, measure in zip(ingredientNames, ingredientMeasures):
        g_ingredientsDB.addIngredientToDB(
            Ingredient(name, measure)
        )
    g_ingredientsDB.updateFile()
    indexesForDelete = [1, 9]
    indexesForDelete.sort(reverse=True)  # Так как индексы смещаются. Лучше думаю делать по имени.
    for index in indexesForDelete:
        print(g_ingredientsDB.getIngredientByID(index).name)
        g_ingredientsDB.deleteIngredientByID(index)
    g_ingredientsDB.updateFile()

    # storage
    g_storage.loadProducts()
    indexesForAddToStotage = [2, 0, 1]
    productAmount = [3, 2, 6]
    for index, amount in zip(indexesForAddToStotage, productAmount):
        g_storage.addProduct(index, amount)
    g_storage.updateFile()
    indexesForDeleteFromStorage = [1, 0]
    indexesForDeleteFromStorage.sort(reverse=True)
    for index in indexesForDeleteFromStorage:
        g_storage.deleteProductByID(index)
    g_storage.updateFile()

    # recipe, book
    recipe = Recipe(
        name='Салат из свежей капусты',
        ingredients={0: 300,
                     1: 1,
                     2: 1,
                     3: 3,
                     4: 3,
                     5: 1,
                     6: 2,
                     7: 1
        },
        cookingSteps={
            1: 'Белокочанную капусту промываем под холодной водой, чистим лук и морковь.',
            2: 'Капусту нарезаем тонкой соломкой.',
            3: 'Морковь натираем на крупной терке, лук нарезаем кубиками, чеснок либо мелко-мелко нарезаем, либо пропускаем через '
               'чесночницу.',
            4: 'Все овощи перекладываем в одну посуду.',
            5: 'Поливаем салат подсолнечным маслом и уксусом, добавляем немножко сахара и соли. Хорошенько перемешиваем.'
        },
        description='Едва ли не самый популярный гарнир к котлетам в простых столовых.'
    )
    # recipe.addIngredient(ingredient)  #либо можно использовать данный метод для добавления ингредиентов
    g_RecipeBook.addRecipe(recipe)
    g_RecipeBook.writeRecipeFile(0)


if __name__ == '__main__':
    log = logger.getLogger(__name__)
    log.debug('start log')
    main()
    with open('logs/log.md', 'a') as file:
        file.write('```')

