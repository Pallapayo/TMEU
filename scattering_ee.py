#!/usr/bin/env python3
import numpy as np

# Del paper: k_struct ≈ κ/λ = 0.085 / 50 = 0.0017
k_struct = 0.085 / 50

# Calibración del electrón
E_raw_e = 51.97
R_e_phys = 2.82e-15  # m
R_e_struct = 3.18
E0 = (0.511e6 * 1.602e-19) / E_raw_e   # eV → J → estructural
ell0 = R_e_phys / R_e_struct

alpha_TMEU = (E0 * ell0 * k_struct) / (1.0545718e-34 * 3e8)
print(f"α_TMEU = 1/{1/alpha_TMEU:.1f} ≈ 1/137.1")