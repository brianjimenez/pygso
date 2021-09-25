"""Module to generate initial populations of glowworms agents used by the GSO algorithm"""

from pygso.swarm import Swarm
from pygso.coordinates import CoordinatesFileReader, Coordinates
from pygso.gso_errors import GSOCoordinatesError
from pygso.landscape import LandscapePosition


class Initializer(object):
    """Generates a population of glowworms.

    The landscape is determined by the ObjectiveFunction object.
    The glowworms will use the given algorithm parameters.
    """

    def __init__(self, objective_functions, number_of_glowworms, gso_parameters):
        self.objective_functions = objective_functions
        self.number_of_glowworms = number_of_glowworms
        self.parameters = gso_parameters
        self.positions = []

    def generate_glowworms(self):
        """Creates an initial population of glowworms"""
        self.positions = self.generate_landscape_positions()
        return Swarm(self.positions, self.parameters)

    def generate_landscape_positions(self):
        """Generates the initial positions of each glowworm"""
        raise NotImplementedError()


class RandomInitializer(Initializer):
    """Generates a population of glowworms with random positions"""

    def __init__(
        self,
        objective_functions,
        number_of_glowworms,
        gso_parameters,
        bounding_box,
        random_number_generator,
    ):
        super(RandomInitializer, self).__init__(
            objective_functions, number_of_glowworms, gso_parameters
        )
        self.bounding_box = bounding_box
        self.random_number_generator = random_number_generator

    def generate_landscape_positions(self):
        """Generates a list of landscape positions that have been read
        from initial_population_file.
        """
        positions = []
        for index in range(self.number_of_glowworms):
            coordinates = []
            for dimension in range(self.bounding_box.dimension):
                bound = self.bounding_box.get_boundary_of_dimension(dimension)
                coord = self.random_number_generator(
                    bound.lower_limit, bound.upper_limit
                )
                coordinates.append(coord)
            positions.append(
                LandscapePosition(self.objective_functions[0], Coordinates(coordinates))
            )
        return [positions]


class FromFileInitializer(Initializer):
    """Generates a population of glowworms with initial positions that
    are read from a given file.
    """

    def __init__(
        self,
        objective_functions,
        number_of_glowworms,
        gso_parameters,
        dimensions,
        initial_population_file,
    ):
        super(FromFileInitializer, self).__init__(
            objective_functions, number_of_glowworms, gso_parameters
        )
        self.dimensions = dimensions
        self.initial_population_file = initial_population_file

    def generate_landscape_positions(self):
        """Generates a list of landscape positions that have been read
        from initial_population_file.
        """
        reader = CoordinatesFileReader(self.dimensions)
        coordinates = reader.get_coordinates_from_file(self.initial_population_file)

        if not coordinates:
            raise GSOCoordinatesError(
                "No coordinates have been read from %s file"
                % self.initial_population_file
            )

        if len(coordinates) != self.number_of_glowworms:
            raise GSOCoordinatesError(
                "Number of coordinates read and number of glowworms does not correspond"
            )

        positions = []
        for index in range(self.number_of_glowworms):
            positions.append(
                LandscapePosition(self.objective_functions[0], coordinates[index])
            )

        return [positions]
