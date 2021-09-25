from math import exp, cos, pi
from pygso.algorithm import GSOBuilder
from pygso.parameters import GSOParameters
from pygso.ofunction import ObjectiveFunction
from pygso.boundaries import BoundingBox, Boundary
from pygso.gso_random import MTGenerator


def found_peaks(
    peak_coordinates, dimension, glowworms, minimum_matches=3, tolerance=0.05
):
    peaks_found = [False for _ in range(len(peak_coordinates))]
    for i_peak, peak in enumerate(peak_coordinates):
        for glowworm in glowworms:
            coordinates = glowworm.landscape_position.coordinates
            found = True
            for j in range(dimension):
                found = found and (abs(coordinates[j] - peak[j]) <= tolerance)
            if found:
                peaks_found[i_peak] = True

    return minimum_matches <= peaks_found.count(True)


def test_j1():
    """Tests the GSO algorithm with the J1 Peaks function"""

    class J1(ObjectiveFunction):
        """Peaks function

        The Peaks function is a function of two variables, obtained by
        translating and scaling Gaussian distributions (Reutskiy and Chen 2006).
        """

        def __call__(self, coordinates):
            return J1.calculate(coordinates[0], coordinates[1])

        @staticmethod
        def calculate(x, y):
            return (
                3.0 * (1 - x) * (1 - x) * exp(-(x * x + (y + 1) * (y + 1)))
                - 10.0 * (x / 5.0 - pow(x, 3) - pow(y, 5)) * exp(-(x * x + y * y))
                - 1 / 3.0 * exp(-((x + 1) * (x + 1) + y * y))
            )

    objective_function = J1()
    bounding_box = BoundingBox([Boundary(-3.0, 3.0), Boundary(-3.0, 3.0)])
    number_of_glowworms = 200
    random_number_generator = MTGenerator(324324)
    builder = GSOBuilder()
    parameters = GSOParameters()
    gso = builder.create(
        number_of_glowworms,
        random_number_generator,
        parameters,
        objective_function,
        bounding_box,
    )

    gso.run(50)

    # Function peak coordinates
    peak_coordinates = [[1.28, 0.0], [0.0, 1.58], [-0.46, -0.63]]

    assert found_peaks(peak_coordinates, 2, gso.swarm.glowworms,
        minimum_matches=2, tolerance=0.1)


def test_rastrigin():

    class Rastrigin(ObjectiveFunction):
        """Rastrigin function"""

        def __call__(self, coordinates):
            return Rastrigin.calculate(coordinates[0], coordinates[1])

        @staticmethod
        def calculate(x, y):
            return (
                20.0 + (x*x - 10.0*cos(2*pi*x) + y*y - 10.0*cos(2*pi*y))
            )

    objective_function = Rastrigin()
    bounding_box = BoundingBox([Boundary(-3.0, 3.0), Boundary(-3.0, 3.0)])
    number_of_glowworms = 200
    seed = 324324
    random_number_generator = MTGenerator(seed)
    builder = GSOBuilder()
    parameters = GSOParameters()
    gso = builder.create(
        number_of_glowworms,
        random_number_generator,
        parameters,
        objective_function,
        bounding_box,
    )

    gso.run(50)

    # Function peak coordinates
    peak_coordinates = [[0.5, 0.5], [1.0, 1.0], [1.5, 1.5], [2.0, 2.0], [2.5, 2.5],
                        [-0.5, -0.5], [-1.0, -1.0], [-1.5, -1.5], [-2.0, -2.0], [-2.5, -2.5],
                        [0.5, -0.5], [1.0, -1.0], [1.5, -1.5], [2.0, -2.0], [2.5, -2.5],
                        [-0.5, 0.5], [-1.0, 1.0], [-1.5, 1.5], [-2.0, 2.0], [-2.5, 2.5]]

    assert found_peaks(peak_coordinates, 2, gso.swarm.glowworms,
        minimum_matches=4, tolerance=0.1)
