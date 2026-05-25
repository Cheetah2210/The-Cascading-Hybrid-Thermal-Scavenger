def near_field_radiative_enhancement(gap_distance, characteristic_wavelength):
    """
    Approximates the near-field radiative enhancement factor due to photon tunneling.
    Far-field limit is 1.0. Near-field scales dramatically as gap d << wavelength.
    """
    if gap_distance <= 0:
        raise ValueError("Gap distance must be greater than zero.")
        
    if gap_distance < characteristic_wavelength:
        # Simplification of evanescent wave coupling enhancement
        enhancement = (characteristic_wavelength / gap_distance)**2
        return min(enhancement, 1000.0)  # Bound by physical material saturation limits
    return 1.0
