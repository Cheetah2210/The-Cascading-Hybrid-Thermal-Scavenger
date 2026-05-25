from thermodynamics import carnot_efficiency
from teg import teg_power

def run_simulation():
    T_hot = 900
    T_cold = 300

    eta = carnot_efficiency(T_hot, T_cold)

    power = teg_power(
        seebeck=0.0002,
        delta_t=T_hot - T_cold,
        resistance=5
    )

    return {
        "efficiency": eta,
        "power": power
    }