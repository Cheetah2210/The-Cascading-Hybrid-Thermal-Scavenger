def thermal_mass_capacity(mass, specific_heat):
    """Calculates total sensible heat storage capacity (Joule/Kelvin)."""
    return mass * specific_heat

def state_of_charge(current_joules, max_joules):
    """Returns normalized capacity metrics."""
    return min(1.0, max(0.0, current_joules / max_joules))
