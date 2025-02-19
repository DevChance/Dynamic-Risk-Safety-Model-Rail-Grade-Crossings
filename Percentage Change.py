import numpy as np

# Define the function for the equation
def calculate_y(CE, MIS):
    return np.exp(0.005 * (1 + (MIS * 2)) * (55 - 5) + 0.000001 * (CE * (1 - (MIS / 50))) - 0.05 * ((0.5) * (1 - (MIS / 5))))

# Define the CE values of interest
CE_values = [0, 200000, 400000, 600000, 800000, 1000000]

# Define the MIS scores
MIS_scores = [0.0, 0.1, 0.25, 0.6, 0.7, 0.75, 0.85, 1.0]

# Compute the base y values for MIS = 0.0
base_y_values = [calculate_y(CE, 0.0) for CE in CE_values]

# Calculate and print the percentage changes
for MIS in MIS_scores:
    print(f"\nPercentage changes for MIS={MIS}:")
    y_values = [calculate_y(CE, MIS) for CE in CE_values]
    for CE, base_y, y in zip(CE_values, base_y_values, y_values):
        percentage_change = ((y - base_y) / base_y) * 100 if base_y != 0 else float('inf')
        print(f"CE={CE:>7} | Base Y={base_y:.4f} | Y with MIS={y:.4f} | Change={percentage_change:.2f}%")
