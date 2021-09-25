class Glowworm(object):
    """Represents a glowworm agent in the algorithm"""

    _created_glowworms = 0

    def __init__(self, landscape_position, gso_parameters):
        """Creates a glowworm agent in the algorithm.

        Starting coordinates are given by landscape_position object.
        """
        self.landscape_position = landscape_position
        self.rho = gso_parameters.rho
        self.gamma = gso_parameters.gamma
        self.beta = gso_parameters.beta
        self.luciferin = gso_parameters.initial_luciferin
        self.vision_range = gso_parameters.initial_vision_range
        self.max_neighbors = gso_parameters.max_neighbors
        self.max_vision_range = gso_parameters.max_vision_range
        self.neighbors = []
        self.probabilities = []
        self.scoring = 0.0
        self.id = Glowworm._created_glowworms
        self.moved = False
        self.step = 0
        Glowworm._created_glowworms += 1

    def search_neighbors(self, glowworms):
        """Searches in a list of glowworms for neighbors of this glowworm"""
        squared_vision_range = self.vision_range * self.vision_range
        self.neighbors = [
            glowworm
            for glowworm in glowworms
            if self.is_neighbor(glowworm, squared_vision_range)
        ]

    def is_neighbor(self, other, squared_vision_range):
        """Defines if a glowworm other is neighbor of this"""
        if self != other and self.luciferin < other.luciferin:
            return self.distance2(other) < squared_vision_range
        return False

    def __eq__(self, other):
        """Compares for equality two glowworms, basically, their id's"""
        return self.id == other.id

    def __ne__(self, other):
        """Compares if this glowworm is not other"""
        return self.id != other.id

    def compute_luciferin(self):
        """Updates luciferin of the current glowworm and returns its value"""
        if self.moved or self.step == 0:
            self.scoring = self.landscape_position.evaluate_objective_function()

        self.luciferin = (1.0 - self.rho) * self.luciferin + self.gamma * self.scoring
        self.step += 1
        return self.luciferin

    def distance(self, other):
        """Calculates the distance between two glowworms"""
        return self.landscape_position.distance(other.landscape_position)

    def distance2(self, other):
        """Calculates the distance^2 between two glowworms"""
        return self.landscape_position.distance2(other.landscape_position)

    def compute_probability_moving_toward_neighbor(self):
        """Computes the probability of this glowworm to move towards any of his neighbors"""
        self.probabilities = []

        total_sum = 0.0
        for neighbor in self.neighbors:
            difference = neighbor.luciferin - self.luciferin
            self.probabilities.append(difference)
            total_sum += difference

        for i in range(len(self.neighbors)):
            self.probabilities[i] /= total_sum

    def select_random_neighbor(self, random_number):
        """Selects a neighbor in the neighbors list using accumulated probabilities of
        moving toward a neighbor."""
        num_neighbors = len(self.neighbors)
        if num_neighbors == 0:
            return self

        sum_probabilities = 0.0
        i = 0
        while sum_probabilities < random_number:
            sum_probabilities += self.probabilities[i]
            i += 1
        return self.neighbors[i - 1]

    def move(self, other, landscape_position=None):
        """Moves towards another glowworm"""
        self.moved = self.id != other.id
        if self.id != other.id:
            if landscape_position:
                self.landscape_position.move(landscape_position)
            else:
                self.landscape_position.move(other.landscape_position)

    def update_vision_range(self):
        """Calculates and updates this glowworm's vision range"""
        self.vision_range = min(
            self.max_vision_range,
            max(
                0.0,
                self.vision_range
                + self.beta * (self.max_neighbors - len(self.neighbors)),
            ),
        )

    def __repr__(self):
        """String representation of a glowworm"""
        return "%s %12.8f %2d %5.3f %12.8f" % (
            str(self.landscape_position),
            self.luciferin,
            len(self.neighbors),
            self.vision_range,
            self.scoring,
        )
