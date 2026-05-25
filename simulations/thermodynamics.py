import numpy as np

SIGMA = 5.670374419e-8

def stefan_boltzmann(T, emissivity=1.0):
    return emissivity * SIGMA * T**4

def carnot_efficiency(T_hot, T_cold):
    return 1 - (T_cold / T_hot)