"""Reads GSO parameters from configuration file"""

from ConfigParser import ConfigParser
import os
from gso_errors import GSOParameteresError


class GSOParameters(object):
    """Represents the set of the variables of the algorithm"""
    def __init__(self, file_name):
        self._config = ConfigParser()
        try:
            self._config.readfp(open(file_name))
        except Exception, e:
            raise GSOParameteresError(str(e))

        try:
            self.rho = float(self._config.get('GSO', 'rho'))
            self.gamma = float(self._config.get('GSO', 'gamma'))
            self.beta = float(self._config.get('GSO', 'beta'))
            self.initial_luciferin = float(self._config.get('GSO', 'initialLuciferin'))
            self.initial_vision_range = float(self._config.get('GSO', 'initialVisionRange'))
            self.max_vision_range = float(self._config.get('GSO', 'maximumVisionRange'))
            self.max_neighbors = int(self._config.get('GSO', 'maximumNeighbors'))

        except Exception, e:
            raise GSOParameteresError("Problem parsing GSO parameters file. Details: %s" % str(e))
