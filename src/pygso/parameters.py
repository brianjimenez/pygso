"""Definition of the algorithm parameters"""


class GSOParameters(object):
    def __init__(
        self,
        rho=0.4,
        gamma=0.6,
        beta=0.08,
        initial_luciferin=0.3,
        initial_vision_range=0.4,
        max_vision_range=0.5,
        max_neighbors=5,
    ):
        self.rho = rho
        self.gamma = gamma
        self.beta = beta
        self.initial_luciferin = initial_luciferin
        self.initial_vision_range = initial_vision_range
        self.max_vision_range = max_vision_range
        self.max_neighbors = max_neighbors
