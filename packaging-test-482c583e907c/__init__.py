try:
    from ._version import *
except ImportError:
    __version__ = version = "0.0.0"
    __version_tuple__ = version_tuple = (0, 0, 0)
