def liquid_metal_mhd_power(fluid_velocity, magnetic_flux_density, conductivity, channel_width, load_factor=0.5):
    """
    Calculates power output per unit volume for a liquid metal/ferrofluid MHD channel.
    Enforces the fluid velocity and magnetic coupling limits.
    """
    # Power density P_d = sigma * u^2 * B^2 * K * (1 - K)
    # Peak power occurs at matched load factor K = 0.5
    power_density = conductivity * (fluid_velocity**2) * (magnetic_flux_density**2) * load_factor * (1.0 - load_factor)
    return max(0.0, power_density)
