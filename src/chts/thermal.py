import numpy as np

SIGMA = 5.670374419e-8  # W/m²·K⁴

def radiative_flux(t_hot, t_cold, emissivity=0.95):
    """Calculates net radiative heat transfer between two surfaces."""
    if t_hot < t_cold:
        raise ValueError("Heat source temperature must exceed sink temperature.")
    return emissivity * SIGMA * (t_hot**4 - t_cold**4)

def conductive_flux(t_hot, t_cold, k_material, thickness, area=1.0):
    """Calculates one-dimensional steady-state conduction (Fourier's Law)."""
    return (k_material * area * (t_hot - t_cold)) / thickness
