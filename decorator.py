import pizza as super_class


class Decorator(super_class.Pizza):
    def __init__(self, description, cost):
        super_class.Pizza.__init__(description, cost)

    def get_cost(self):
        return super_class.Pizza.get_cost(self)

    def get_description(self):
        return super_class.Pizza.get_description(self)
