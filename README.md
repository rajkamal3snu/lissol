1D Poisson Solver — Finite Difference Validation
A minimal Python demonstration of the one-dimensional, charge-free Poisson equation (Laplace equation) with fixed-potential (Dirichlet) boundary conditions.
This repository is a teaching and numerical-validation example and is not yet a VASPsol implementation, a Li–S battery solvation model, or a solver with mobile ions or spatially varying dielectric properties.

A minimal Python demonstration of the one-dimensional, **charge-free** Poisson equation (Laplace equation) with fixed-potential (Dirichlet) boundary conditions.

This repository is a teaching and numerical-validation example and is **not yet a VASPsol implementation, a Li–S battery solvation model, or a solver with mobile ions or spatially varying dielectric properties**.

## Mathematical model

The electrostatic potential satisfies

$$
\frac{d}{dx}\left[\varepsilon_0\varepsilon_r\frac{d\phi(x)}{dx}\right]=-\rho_{\mathrm{free}}(x).
$$

For a constant relative permittivity $\varepsilon_r>0$ and zero free charge $\rho_{\mathrm{free}}=0$:

$$
\frac{d^2\phi}{dx^2}=0.
$$

With $\phi(0)=\phi_L$ and $\phi(L)=\phi_R$, the exact solution is

$$
\phi(x)=\phi_L+(\phi_R-\phi_L)\frac{x}{L}.
$$

At interior grid point $i$, the centered finite-difference discretization is

$$
-\phi_{i-1}+2\phi_i-\phi_{i+1}=0.
$$

This gives a tridiagonal linear system. The boundary values are included in the right-hand side. Because the dielectric is uniform and there is no free charge, $\varepsilon_r$ cancels from this equation; **changing `epsilon_r` does not change the resulting potential in this example**.

## Requirements

- Python 3.9 or newer
- NumPy

## Installation and use

```bash
python -m pip install -r requirements.txt
python poisson_1d.py
```

Example output includes the maximum difference between the numerical and analytical linear profiles, the potential at the center, and a `PASS` assertion for an error smaller than `1e-10`.

## Tests

```bash
python -m unittest discover -s tests -v
```

## Project files

- `poisson_1d.py`: numerical solver and analytical validation
- `tests/test_poisson_1d.py`: regression and input-validation tests
- `requirements.txt`: Python dependency


Python 3.9 or newer
NumPy
Installation and use
```bash
python -m pip install -r requirements.txt
python poisson_1d.py
```
Example output includes the maximum difference between the numerical and analytical linear profiles, the potential at the center, and a `PASS` assertion for an error smaller than `1e-10`.
Tests
```bash
python -m unittest discover -s tests -v
```
Project files
`poisson_1d.py`: numerical solver and analytical validation
`tests/test_poisson_1d.py`: regression and input-validation tests
`requirements.txt`: Python dependency
Next research steps
For electrolyte or Li–S battery applications, a next-stage model would need a spatially varying dielectric response, nonzero charge density, and physically motivated boundary conditions. Mobile-ion descriptions and interfaces require additional physics and validation.
