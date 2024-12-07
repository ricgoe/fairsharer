import numpy as np

def fair_sharer(values: list | np.ndarray, num_iterations: int, share: float = 0.1):
    """Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neightbor of the rightmost field.
    
    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    
    Args
    values:
        1D array of values (list or numpy array)
    num_iteration:
        Integer to set the number of iterations
    """
    if not isinstance(values, (list, np.ndarray)):
        raise TypeError(f"'values' must be of type list or numpy.ndarray, not {type(values).__name__}")
    if not isinstance(num_iterations, int):
        raise TypeError(f"'num_iterations' must be an integer, not {type(num_iterations).__name__}")
    if not isinstance(share, (float, int)):
        raise TypeError(f"'share' must be a float, not {type(share).__name__}")
    if not(0 < share <= 1):
        raise ValueError(f"'share' must be between 0 and 1, not {share}")

    values_new = list(values)
    for _ in range(num_iterations):
        max_val = max(values_new)
        idx_max = values_new.index(max_val)
        idx_to_check = [(idx_max-1)%len(values), (idx_max+1)%len(values)]
        values_new = [val+max_val*share if idx in idx_to_check else val for idx, val in enumerate(values_new)]
        values_new[idx_max] -= 2*max_val*share
    return values_new

if __name__ == "__main__":
    print(fair_sharer(np.array([0, 1000, 800, 0]), 1))