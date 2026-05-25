def verify_second_law_compliance(t_source, t_sink, electrical_power_out, total_heat_in):
    """
    Strict structural gatekeeper. Returns True if the simulation complies 
    with the Second Law of Thermodynamics, False if it violates physics.
    """
    actual_efficiency = electrical_power_out / total_heat_in
    carnot_limit = 1.0 - (t_sink / t_source)
    
    if actual_efficiency >= carnot_limit:
        print(f"CRITICAL ERROR: System efficiency ({actual_efficiency*100:.2f}%) "
              f"violates the Carnot Limit ({carnot_limit*100:.2f}%). Check loop logic.")
        return False
    return True
