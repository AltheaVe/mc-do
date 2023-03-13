from mcdo.burger import Burger

class Customer:

    def __init__(self, restrictions=[]):
        self.restrictions = restrictions

    def order(self):
        burger = Burger()
        for restriction in self.restrictions:
            burger.transform(restriction)

        burger.display()
