import pytest
import os
import numpy as np

from ..gaussian_elimination import gaussian_elimination


@pytest.fixture()
def input_file():
    file_path = os.path.join(os.path.dirname(__file__), "test_data/coefficients.csv")
    return file_path


class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def test_gaussian_elimination(input_file):
    no_unknowns = 4
    args = Namespace(n=no_unknowns, coeffs=input_file)

    solution = gaussian_elimination(args)
    for sol, val in zip(solution, np.array([16, -6, -2, -3])):
        assert sol == val
