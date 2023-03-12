import decorator as decorator_class


class Olive(decorator_class.Decorator):
    def __init__(self):
        self.description = "Olive Sauce"
        self.cost = 5


class Mushroom(decorator_class.Decorator):
    def __init__(self):
        self.description = "Mushrooms Sauce"
        self.cost = 7


class GoatCheese(decorator_class.Decorator):
    def __init__(self):
        self.description = "Goat Cheese Sauce"
        self.cost = 12


class Meat(decorator_class.Decorator):
    def __init__(self):
        self.description = "Meat Sauce"
        self.cost = 26


class Onion(decorator_class.Decorator):
    def __init__(self):
        self.description = "Onions Sauce"
        self.cost = 17


class Corn(decorator_class.Decorator):
    def __init__(self):
        self.description = "Corn Sauce"
        self.cost = 20
