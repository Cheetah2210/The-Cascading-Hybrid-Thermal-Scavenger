def teg_power(seebeck, delta_t, resistance):
    voltage = seebeck * delta_t
    power = (voltage ** 2) / resistance
    return power