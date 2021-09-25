from pygso.algorithm import GSOBuilder
from pygso.parameters import GSOParameters
from pygso.ofunction import J1
from pygso.boundaries import BoundingBox, Boundary
from pygso.gso_random import MTGenerator


def found_peaks(
    peak_coordinates, dimension, glowworms, minimum_matches=3, tolerance=0.05
):
    peaks_found = [False for _ in range(len(peak_coordinates))]
    for i_peak, peak in enumerate(peak_coordinates):
        for glowworm in glowworms:
            coordinates = glowworm.landscape_positions[0].coordinates
            found = True
            for j in range(dimension):
                found = found and (abs(coordinates[j] - peak[j]) <= tolerance)
            if found:
                peaks_found[i_peak] = True

    return minimum_matches <= peaks_found.count(True)


def test_j1():
    """Tests the GSO algorithm with the J1 Peaks function"""
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

    gso.run(100)

    # Function peak coordinates
    peak_coordinates = [[1.28, 0.0], [0.0, 1.58], [-0.46, -0.63]]

    assert found_peaks(peak_coordinates, 1, gso.swarm.glowworms)
