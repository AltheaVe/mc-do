class Burger:

    def __init__(self):
        self.ingredients = {'bun' : 'bun', 'sauce' : 'sauce', 'cheese' : 'cheese', 'steak' : 'steak', 'tomato' : 'tomato', 'salad' : 'salad'}
        self.transform_types = {'gluten_free' : self.transform_gluten_free, 'vegetarian' : self.transform_vegetarian, 'lactose_intolerant' : self.transform_lactose_intolerant}

    def transform(self, restriction):
        self.transform_types[restriction]()

    def transform_gluten_free(self):
        self.ingredients['bun'] = 'bun gluten_free'

    def transform_vegetarian(self):
        self.ingredients['steak'] = 'steak vegetarian'

    def transform_lactose_intolerant(self):
        del self.ingredients['cheese']

    def display(self):
        for ingredient, type in self.ingredients.items():
            print(type)
        print(self.ingredients['sauce'])
        print(self.ingredients['bun'])
        print('')
