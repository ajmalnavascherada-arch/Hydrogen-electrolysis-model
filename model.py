import numpy as np

FARADAY_CONST = 96485  # C/mol

def hydrogen_production(current):
    """
    Calculate hydrogen production rate (mol/s)
    """
    return current / (2 * FARADAY_CONST)


def electrolyzer_power(voltage, current):
    """
    Power consumption (W)
    """
    return voltage * current


def efficiency(ideal_voltage, actual_voltage):
    """
    Efficiency of electrolyzer
    """
    return ideal_voltage / actual_voltage