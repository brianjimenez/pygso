from math import sqrt


def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    """Compare two float numbers"""
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def sum_of_squares(values):
    """Calculates the sum of squares of each value in values"""
    return sum(map(lambda x: x*x, values))


def norm(values):
    """Calculates the norm of the given values"""
    return sqrt(sum_of_squares(values))


def sum_of_square_difference(v1, v2):
    """Calculates the sum of the square differences of the components of
    v1 and v2 vectors.
    """
    sum = 0.0
    for c1, c2 in zip(v1, v2):
        t = c1-c2
        sum += t*t
    return sum


def distance(double x1, double y1, double z1, double x2, double y2, double z2):
    """Calculates the distance between point 1 and point 2."""
    return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) + (z1-z2)*(z1-z2))


def distance2(double x1, double y1, double z1, double x2, double y2, double z2):
    """Calculates the distance^2 between point 1 and point 2."""
    return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) + (z1-z2)*(z1-z2)
