import unittest

import numpy as np

from poisson_1d import solve_poisson_1d


class TestPoisson1D(unittest.TestCase):
    def test_linear_solution(self):
        x, phi = solve_poisson_1d(phi_left=1.5, phi_right=-0.5)
        exact = 1.5 + (-0.5 - 1.5) * x / x[-1]
        np.testing.assert_allclose(phi, exact, atol=1e-12, rtol=0)

    def test_invalid_grid(self):
        with self.assertRaises(ValueError):
            solve_poisson_1d(num_points=2)


if __name__ == "__main__":
    unittest.main()
