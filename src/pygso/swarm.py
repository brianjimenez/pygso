"""A swarm is a collection of glowworms"""

from os import linesep
from pathlib import Path
from pygso.glowworm import Glowworm


class Swarm(object):
    """A swarm of glowworms"""

    def __init__(self, landscape_positions, parameters):
        """Creates a population of glowworms using a list of landscape_positons and GSO parameters"""
        positions_per_glowworm = [[] for _ in range(len(landscape_positions[0]))]
        for function in landscape_positions:
            for glowworm_id, position in enumerate(function):
                positions_per_glowworm[glowworm_id].append(position)
        self.glowworms = [
            Glowworm(positions, parameters) for positions in positions_per_glowworm
        ]
        self.docking = (
            landscape_positions[0][0].__class__.__name__ != "LandscapePosition"
        )

    def update_luciferin(self):
        """Updates luciferin of each glowworm in this swarm"""
        for glowworm in self.glowworms:
            glowworm.compute_luciferin()

    def movement_phase(self, rnd_generator):
        """Updates luciferin and probabilities of each glowworm to move if required
        following GSO algorithm
        """
        selected = []
        positions = {}
        num_glowworms = self.get_size()
        for i in range(num_glowworms):
            glowworm = self.glowworms[i]
            glowworm.search_neighbors(self.glowworms)
            glowworm.compute_probability_moving_toward_neighbor()
            selected.append(glowworm.select_random_neighbor(rnd_generator()))
            positions[i] = [
                landscape_position.clone()
                for landscape_position in selected[-1].landscape_positions
            ]

        for i in range(num_glowworms):
            glowworm = self.glowworms[i]
            neighbor = selected[i]
            position = positions[i]
            glowworm.move(neighbor, position)
            glowworm.update_conformers(neighbor, rnd_generator)
            glowworm.update_vision_range()

    def get_size(self):
        """Gets the population size of this swarm of glowworms"""
        return len(self.glowworms)

    def save(self, step, destination_path, file_name=""):
        """Saves actual population status to a file"""
        if file_name:
            dest_file_name = Path(destination_path) / file_name
        else:
            dest_file_name = Path(destination_path) / f"gso_{step}.out"

        dest_file = open(dest_file_name, "w")
        dest_file.write(str(self))
        dest_file.close()

    def __repr__(self):
        """String representation of the population"""
        representation = (
            "#Coordinates  Luciferin  Neighbor's number  Vision Range  Scoring"
        ) + linesep
        for glowworm in self.glowworms:
            representation += str(glowworm) + linesep
        return representation
