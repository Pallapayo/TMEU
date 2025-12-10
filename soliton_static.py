
#### `soliton_static.py` ← el corazón, reproduce la Tabla 1 del paper
```python
#!/usr/bin/env python3
import numpy as np
from scipy.optimize import minimize
from scipy.integrate import simpson
import argparse

lambda_val = 50.0
kappa = 0.085

def energy_w(w, R=3.18, a=0.12, sigma=1.1):
    r = np.linspace(1e-6, 30, 5000)
    phi = 1 - a * np.exp(-r**2 / sigma**2)
    theta = w * np.arctan2(0, r) + np.pi * (1 - np.exp(-r / R))  # winding w
    dphi_dr = -a * (-2*r / sigma**2) * np.exp(-r**2 / sigma**2)
    nabla_theta_sq = (w / r)**2 + (np.pi / R * np.exp(-r / R))**2
    nabla_theta_4 = nabla_theta_sq**2

    integrand = 2*np.pi*r * (
        0.5 * dphi_dr**2 +
        (lambda_val/4) * (phi**2 - 1)**2 +
        0.5 * phi**2 * nabla_theta_sq +
        (kappa/4) * phi**4 * nabla_theta_4
    )
    return simpson(integrand, r)

# Tabla del paper
particles = { "Electrón":1, "Muón":14, "Tauón":59, "Protón":43 }
for name, w in particles.items():
    E = energy_w(w)
    print(f"{name:8} w={w:3d} → E_struct = {E:8.2f}")