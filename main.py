from RecipeBook import *

ingredientData = {}
ingredientData['id'] = 0
ingredientData['name'] = 'apple'
ingredientData['amount'] = 1
ingredientData['measure'] = 'thing'
ingredient = Ingredient(ingredientData)

recipeData = {}
recipeData['id'] = 0
recipeData['name'] = 'Apple slices'
recipeData['ingredients'] = [ingredient]
# or recipe['ingredients'] = [] after
# recipe['ingredients'].append(ingredient)
recipeData['cookingSteps'] = None
recipeData['description'] = None
print(recipeData)
g_RecipeBook.createRecipe(recipeData)