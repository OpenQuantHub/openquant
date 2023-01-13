import numpy as np


def geometric_mean(iterable):
    """Calculate the geometric mean of iterable."""
    return np.array(iterable).prod()**(1.0/len(iterable))
