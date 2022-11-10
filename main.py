from logger import logger
from RecipeBook import g_RecipeBook, Ingredient, Recipe
from ingredientsDB import g_ingredientsDB


def main():
    ingredient = g_ingredientsDB.addIngredientToDB(
        Ingredient(
            name='apple',
            amount=1,
            measure='thing'
        )
    )

    recipe = Recipe(
        name='Apple slices',
        ingredients=[],
        cookingSteps=None,
        description=None
    )

    recipe.addIngredient(ingredient)
    g_RecipeBook.addRecipe(recipe)


if __name__ == '__main__':
    logger.setLogMode('w+')
    log = logger.getLogger(__name__)
    log.debug('start log')
    main()

