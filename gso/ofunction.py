"""The objective function to optimize using the GSO algorithm"""

from math import exp


class ObjectiveFunction(object):
    """Objective functions interface"""
    def __call__(self, coordinates):
        raise NotImplementedError()


class J1(ObjectiveFunction):
    """Peaks function

    The Peaks function is a function of two variables, obtained by
    translating and scaling Gaussian distributions (Reutskiy and Chen 2006).
    """
    def __call__(self, coordinates):
        return J1.j1(coordinates[0], coordinates[1])

    @staticmethod
    def j1(x, y):
        return 3.0 * (1-x)*(1-x) * exp(-(x*x + (y+1)*(y+1))) \
               - 10.0 * (x/5.0 - pow(x,3) - pow(y,5)) * exp(-(x*x + y*y)) \
               - 1/3.0 * exp(-((x+1)*(x+1) + y*y))
