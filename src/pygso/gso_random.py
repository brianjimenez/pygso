"""Random number generator class for wrapping Python implementation"""

import random


class RandomNumberGenerator(object):
    """Random number generator interface"""

    def __call__(self):
        raise NotImplementedError()


class MTGenerator(RandomNumberGenerator):
    """Python uses the Mersenne Twister as the core generator.
    It produces 53-bit precision floats and has a period of 2**19937-1
    """

    def __init__(self, seed):
        self.seed = seed
        self.random = random.Random(seed)

    def __call__(self, lower_limit=0.0, upper_limit=1.0):
        return self.random.uniform(lower_limit, upper_limit)

    def randint(self, lower_limit=0, upper_limit=9):
        return self.random.randint(lower_limit, upper_limit)
