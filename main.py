import numpy as np
import matplotlib.pyplot as plt
from model import hydrogen_production, electrolyzer_power, efficiency

# Parameters
current_range = np.linspace(10, 200, 50)  # Amps
voltage = 1.8  # realistic electrolyzer voltage
ideal_voltage = 1.23  # thermodynamic voltage

h2_rates = []
efficiencies = []

for current in current_range:
    h2 = hydrogen_production(current)
    eff = efficiency(ideal_voltage, voltage)

    h2_rates.append(h2)
    efficiencies.append(eff)

# Plot results
plt.figure()
plt.plot(current_range, h2_rates)
plt.xlabel("Current (A)")
plt.ylabel("Hydrogen Production (mol/s)")
plt.title("Hydrogen Production vs Current")
plt.grid()
plt.savefig("results/h2_production.png")
plt.show()