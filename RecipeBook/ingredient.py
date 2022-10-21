class Ingredient:

    def __init__(self, args):
        """args - json format:
            {
                'id': id,
                'name': name,
                'amount': amount,
                'measure': measure
            }
        """
        self._id = args.get('id')
        self._name = args.get('name')
        self._amount = args.get('amount')
        self._measure = args.get('measure')
