"""Custom error classes"""


class GSOError(Exception):
    """GSO exception base class"""
    def __init__(self, cause):
        self.cause = cause

    def __str__(self):
        representation = "[%s] %s" % (self.__class__.__name__, self.cause)
        return representation


class GSOParameteresError(GSOError):
    """Custom GSOParameteres exception"""
    pass


class GSOCoordinatesError(GSOError):
    """Custom error for CoordinatesFileReader class"""
    pass


class RandomNumberError(GSOError):
    """Custom error for random number generation"""
    pass
