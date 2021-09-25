"""Objective function landscape representations"""


class LandscapePosition(object):
    """Represents glowworm's current position in the objective function space.

    Distance operation is defined for a Cartesian space of N dimensions.
    Different spaces should implement different approaches for move() and
    distance() functions.
    """

    def __init__(self, objective_function, coordinates, step=0.5):
        self.objective_function = objective_function
        self.coordinates = coordinates
        self.step = step

    def evaluate_objective_function(self):
        """Evaluates the objective function at the given coordinates"""
        return self.objective_function(self.coordinates)

    def __eq__(self, other):
        """Compares for equality two landscape positions"""
        return (
            self.coordinates == other.coordinates
            and self.objective_function == other.objective_function
        )

    def __ne__(self, other):
        """Compares for unequality two landscape positions"""
        return not self.__eq__(other)

    def clone(self):
        """Creates a copy of this landscape position"""
        return LandscapePosition(
            self.objective_function, self.coordinates.clone(), self.step
        )

    def __add__(self, other):
        """Adds two landscape positions"""
        return LandscapePosition(
            self.objective_function, self.coordinates + other.coordinates
        )

    def __iadd__(self, other):
        """Adds other to the current landscape position"""
        self.coordinates += other.coordinates
        return self

    def __sub__(self, other):
        """Subtracts two landscape positions"""
        return LandscapePosition(
            self.objective_function, self.coordinates - other.coordinates
        )

    def __isub__(self, other):
        """Subtracts other to the current landscape position"""
        self.coordinates -= other.coordinates
        return self

    def __mul__(self, scalar):
        """Multiplies this landscape position by a scalar"""
        return LandscapePosition(self.objective_function, self.coordinates * scalar)

    def norm(self):
        """Calculates the norm of the coordinates of this landscape position"""
        return self.coordinates.norm()

    def distance(self, other):
        """Calculates the distance between this landscape position and other"""
        delta_x = other - self
        return delta_x.coordinates.norm()

    def distance2(self, other):
        """Calculates the distance^2 between this landscape position and other"""
        delta_x = other - self
        return delta_x.coordinates.sum_of_squares()

    def move(self, other):
        """Move from this landscape position to another given a fixed step"""
        if self != other:
            delta_x = other - self
            delta_x *= self.step / delta_x.norm()
            self += delta_x
        return self

    def update_conformers(self, other, rnd_generator=None, current_scoring=0):
        """Compatibility with GSO test function tests"""
        pass

    def __repr__(self):
        return str(self.coordinates)
