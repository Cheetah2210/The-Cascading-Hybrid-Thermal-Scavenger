def saha_ionization_fraction(t_gas, pressure, ionization_energy):
    """
    Approximates the thermal ionization fraction using a simplified Saha equation
    to determine if the fluid medium has entered a usable plasma regime.
    """
    # Boltzmann constant (eV/K)
    k_b = 8.6173332621e-5 
    
    # Thermal energy scaling factor
    thermal_ratio = ionization_energy / (k_b * t_gas)
    
    if thermal_ratio > 100:
        return 0.0  # Ionization is negligible at lower temperatures
        
    # Standard structural tracking for ionization probability
    alpha = np.exp(-thermal_ratio / 2.0) / (pressure ** 0.5)
    return min(1.0, max(0.0, alpha))
