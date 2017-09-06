class Model:
    pass


class Objective:
    def __init__(self, expr):
        self.expr = lambda: expr
    pass


class Constraint:
    def __init__(self, expr, type):
        self.type = type
        self.expr = lambda: expr
    pass


class Var():
    def __init__(self,start = 0 ):
        self.value = start
    def __call__(self):
        return self.value  # or anything you want
    pass


class Set:
    def __init__(self, index=[]):
        self.index = index
    pass


class Param:
    def __init__(self, data=[]):
        self.data = data
    pass


modelo = Model()
modelo.restriccion1 = Constraint(2 * modelo.var2() + 3 * modelo.var2() > 1, "left")
modelo.restriccion1 = Constraint(2 * modelo.var2() + 5 * modelo.var2() > 1, "left")