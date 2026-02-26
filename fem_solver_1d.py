# ===================================
# 1D FEM Solver — 2 Element Bar
# By Chintan
# This is real Finite Element Method!
# ===================================

import numpy as np
import matplotlib.pyplot as plt

print("=== 1D FEM SOLVER ===")
print("2-Element Bar Problem\n")
print("Structure: [Node1]---Element1---[Node2]---Element2---[Node3]")
print("           Fixed                                    Force Applied\n")

# Material input
E = float(input("Enter Young's Modulus (MPa) [Steel=210000]: "))
A = float(input("Enter cross-sectional area (mm²): "))

# Geometry input
L1 = float(input("Enter length of Element 1 (mm): "))
L2 = float(input("Enter length of Element 2 (mm): "))

# Force input
F = float(input("Enter applied force at Node 3 (N): "))

# ===================================
# FEM CALCULATION
# ===================================

# Element stiffness values
k1 = (A * E) / L1
k2 = (A * E) / L2

print(f"\nElement 1 stiffness: {k1:.2f} N/mm")
print(f"Element 2 stiffness: {k2:.2f} N/mm")

# Global stiffness matrix assembly (3x3)
K = np.array([
    [ k1,      -k1,       0],
    [-k1,  k1 + k2,     -k2],
    [  0,      -k2,      k2]
])

print(f"\nGlobal Stiffness Matrix K:")
print(K)

# Force vector
F_vector = np.array([0, 0, F])

# Apply boundary condition — Node 1 is fixed (u1 = 0)
# Remove first row and column
K_reduced = K[1:, 1:]
F_reduced = F_vector[1:]

# Solve for displacements
displacements_free = np.linalg.solve(K_reduced, F_reduced)

# Full displacement vector
u = np.array([0, displacements_free[0], displacements_free[1]])

print(f"\n--- DISPLACEMENT RESULTS ---")
print(f"Node 1 displacement: {u[0]:.4f} mm (Fixed)")
print(f"Node 2 displacement: {u[1]:.4f} mm")
print(f"Node 3 displacement: {u[2]:.4f} mm")

# Calculate element stresses
stress1 = E * (u[1] - u[0]) / L1
stress2 = E * (u[2] - u[1]) / L2

print(f"\n--- STRESS RESULTS ---")
print(f"Element 1 stress: {stress1:.2f} MPa")
print(f"Element 2 stress: {stress2:.2f} MPa")

# ===================================
# VISUALIZATION
# ===================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1 — Displacement diagram
node_positions = [0, L1, L1 + L2]
ax1.plot(node_positions, u, 'bo-', linewidth=2,
         markersize=10, label='Displaced shape')
ax1.plot(node_positions, [0, 0, 0], 'r--',
         linewidth=1.5, label='Original shape')
ax1.set_title("Displacement Along Bar")
ax1.set_xlabel("Position (mm)")
ax1.set_ylabel("Displacement (mm)")
ax1.legend()
ax1.grid(True)

# Plot 2 — Stress diagram
element_centers = [L1/2, L1 + L2/2]
stresses = [stress1, stress2]
colors = ['green' if s < 250 else 'red' for s in stresses]
ax2.bar(["Element 1", "Element 2"], stresses,
        color=colors, edgecolor='black', linewidth=1.2)
ax2.axhline(y=250, color='red', linestyle='--',
            linewidth=2, label='Yield Strength (250 MPa)')
ax2.set_title("Stress in Each Element")
ax2.set_xlabel("Element")
ax2.set_ylabel("Stress (MPa)")
ax2.legend()
ax2.grid(True, axis='y')

plt.suptitle("1D FEM Analysis Results — By Chintan",
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()