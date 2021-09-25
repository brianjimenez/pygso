"""Reads GSO parameters from configuration file"""

from configparser import ConfigParser
from pygso.gso_errors import GSOParameteresError


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


class GSOFileParameters(object):
    """Represents the set of the variables of the algorithm"""

    def __init__(self, file_name):
        self._config = ConfigParser()
        try:
            self._config.readfp(open(file_name))
        except Exception as e:
            raise GSOParameteresError(str(e))

        try:
            self.rho = float(self._config.get("GSO", "rho"))
            self.gamma = float(self._config.get("GSO", "gamma"))
            self.beta = float(self._config.get("GSO", "beta"))
            self.initial_luciferin = float(self._config.get("GSO", "initialLuciferin"))
            self.initial_vision_range = float(
                self._config.get("GSO", "initialVisionRange")
            )
            self.max_vision_range = float(self._config.get("GSO", "maximumVisionRange"))
            self.max_neighbors = int(self._config.get("GSO", "maximumNeighbors"))

        except Exception as e:
            raise GSOParameteresError(
                "Problem parsing GSO parameters file. Details: %s" % str(e)
            )
