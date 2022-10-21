class Recipe:

    def __init__(self, args):
        """args - json format:
        {
            'id': id,
            'name': name,
            'ingredients': [
                {
                    ingredientId: id,
                    ingredientName: name,
                    ingredientAmount: amount,
                    ingredientMeasure: measure
                },
            ],
            'cookingSteps': cookingSteps,
            'description': description
        }
        """
        self._id = args.get('id')
        self._name = args.get('name')
        self._ingredients = args.get('ingredients')
        self._cookingSteps = args.get('cookingSteps')
        self._description = args.get('description')
