from src.fair import fair_sharer
import pytest
import numpy as np

@pytest.mark.parametrize("values, num_iterations, expected", [
    ([0, 1000, 800, 0], 1, [100, 800, 900, 0]),
    ([0, 1000, 800, 0], 2, [100, 890, 720, 90]),
    (np.array([0, 1000, 800, 0]), 1, [100, 800, 900, 0]),
])
def test_fair_sharer(values, num_iterations, expected):
    assert fair_sharer(values, num_iterations) == expected
    
def test_fair_sharer_invalid_values():
    with pytest.raises(TypeError, match="'values' must be of type list or numpy.ndarray"):
        fair_sharer("teststring", 10, 0.1)

def test_fair_sharer_invalid_num_iterations():
    with pytest.raises(TypeError, match="'num_iterations' must be an integer"):
        fair_sharer([1, 2, 3], "10", 0.1)

def test_fair_sharer_invalid_share():
    with pytest.raises(TypeError, match="'share' must be a float"):
        fair_sharer([1, 2, 3], 10, "0.1")