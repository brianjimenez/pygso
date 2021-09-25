"""Definition of the algorithm parameters"""


class GSOParameters(object):
    def __init__(
        self,
        rho=0.1,
        gamma=0.2,
        beta=0.6,
        initial_luciferin=0.3,
        initial_vision_range=0.4,
        max_vision_range=0.5,
        max_neighbors=7,
    ):
        self.rho = rho
        self.gamma = gamma
        self.beta = beta
        self.initial_luciferin = initial_luciferin
        self.initial_vision_range = initial_vision_range
        self.max_vision_range = max_vision_range
        self.max_neighbors = max_neighbors
