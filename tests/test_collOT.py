import numpy as np
import pytest
from src import collOT_numpy, total_cost, change_cost

def test_total_cost_symmetric():
    # Create two identical marginals (distance should be zero)
    x = np.zeros((2, 4, 3))  # Nm=2, Np=4, dim=3
    ids = np.array([[i for i in range(4)] for _ in range(2)])
    cost = total_cost(x, ids)
    assert cost == 0.0

def test_change_cost_reduces_when_swapping_identical_points():
    x = np.zeros((3, 4, 2))
    ids = np.array([[i for i in range(4)] for _ in range(3)])
    i1s = np.array([0, 1])
    i2s = np.array([2, 3])
    k = 1
    before = change_cost(x, ids, i1s, i2s, k, before=True)
    after = change_cost(x, ids, i1s, i2s, k, before=False)
    assert np.allclose(before, after)  # identical points → no change

def test_collOT_numpy_runs_and_reduces_cost():
    rng = np.random.default_rng(0)
    x = rng.normal(size=(3, 6, 2))  # Nm=3, Np=6, dim=2
    x_copy = x.copy()

    initial_cost = total_cost(x_copy, None)
    result_x, dists_coll, nt = collOT_numpy(x_copy)

    assert isinstance(result_x, np.ndarray)
    assert len(dists_coll) >= 1
    assert nt >= 1
    # Cost should not increase
    assert dists_coll[-1] <= dists_coll[0] + 1e-8

