import pizza as super_class


class ClassicPizza(super_class.Pizza):
    def __init__(self):
        description = "Classic Pizza"
        cost = 80
        super().__init__(description, cost)


class MargheritaPizza(super_class.Pizza):
    def __init__(self):
        description = "Margherita Pizza"
        cost = 130
        super().__init__(description, cost)


class TurkishPizza(super_class.Pizza):
    def __init__(self):
        description = "Turkish Pizza"
        cost = 150
        super().__init__(description, cost)


class PlainPizza(super_class.Pizza):
    def __init__(self):
        description = "Plain Pizza"
        cost = 100
        super().__init__(description, cost)
