"""
Model
=====

This module contains all the basic classes to work and define a correct model for PyOptimizer

Example:
modelo = Model()
modelo.restriccion1 = Constraint(2 * modelo.var2() + 3 * modelo.var2() > 1, "left")
modelo.restriccion1 = Constraint(2 * modelo.var2() + 5 * modelo.var2() > 1, "left")

"""

class Model:
    """
    Modelo
    =========
    es la clase principal que debe contener en sus atributos todo lo necesario para un modelo de optimizacion

    """

    pass


class Objective:
    """
    Funcion Objectivo
    =========
    es la funcion principal del modelo que se intenta minimizar

    Atributos
    *expr: es una funcion anonima que contiene la expresion matematica
    """

    def __init__(self, expr):
        self.expr = lambda: expr
    pass


class Constraint:
    """
    Restricciones
    =========
    representan las fronteras de decision del modelo

    Atributos
    *expr: es la expresion matematica que define la restriccion
    *type: se refiere al tipo de restriccion que presenta
    """

    def __init__(self, expr, type):
        self.type = type
        self.expr = lambda: expr
    pass


class Var:
    """
    Variables
    =========
    se utilizan en el modelo como variables de decision

    Atributos
    *value: es el valor que tiene la variable durante todo el proceso de optimizacion
    """
    def __init__(self,start = 0 ):
        self.value = start
    def __call__(self):
        return self.value
    pass


class Set:
    """
    Sets
    =========
    se utilizan en el modelo como indices para las variables de decision

    Atributos
    *index: es un array unidimensional que contiene los indices de una variable de decicsion
    """
    def __init__(self, index=[]):
        self.index = index
    pass
    def __call__(self):
        return self.index
    pass

class Param:
    """
    Parametros
    =========
    se utilizan en el modelo como constantes de las restricciones

    Atributos
    *data: es el valor que tiene el parametro para cada restriccion
    """
    def __init__(self, data=[]):
        self.data = data
    pass
    def __call__(self):
        return self.data
    pass



if __name__ == "__main__":
    import doctest
    doctest.testmod()