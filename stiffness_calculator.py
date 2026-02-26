# ===================================
# Bar Stiffness Calculator
# By Chintan
# Formula: k = AE/L
# This is the foundation of FEM!
# ===================================

import matplotlib.pyplot as plt
import numpy as np

# Material properties (Young's Modulus in MPa)
materials = {
    "1": ("Mild Steel",  210000),
    "2": ("Aluminum",     70000),
    "3": ("Titanium",    110000),
    "4": ("Cast Iron",   100000),
}

print("=== BAR STIFFNESS CALCULATOR ===")
print("Formula: k = AE/L\n")
print("Select Material:")
for key, (name, E) in materials.items():
    print(f"  {key}. {name} (E = {E} MPa)")

choice = input("\nEnter choice (1-4): ")
material_name, E = materials[choice]

# Input values
A = float(input("Enter cross-sectional area (mm²): "))
L = float(input("Enter length of bar (mm): "))

# Calculate stiffness
k = (A * E) / L

# Calculate displacement for different forces
force = float(input("Enter applied force (N): "))
displacement = force / k

print(f"\n--- RESULTS ---")
print(f"Material        : {material_name}")
print(f"Young's Modulus : {E} MPa")
print(f"Area            : {A} mm²")
print(f"Length          : {L} mm")
print(f"Stiffness k     : {k:.2f} N/mm")
print(f"Applied Force   : {force} N")
print(f"Displacement    : {displacement:.4f} mm")

# Plot displacement vs force
forces = np.linspace(0, force * 2, 100)
displacements = forces / k

plt.figure(figsize=(8, 5))
plt.plot(displacements, forces, color='blue',
         linewidth=2, label=f'k = {k:.0f} N/mm')
plt.axvline(x=displacement, color='green', linestyle='--',
            linewidth=1.5, label=f'Your displacement ({displacement:.4f} mm)')
plt.axhline(y=force, color='red', linestyle='--',
            linewidth=1.5, label=f'Your force ({force:.0f} N)')
plt.title(f"Force vs Displacement — {material_name}")
plt.xlabel("Displacement (mm)")
plt.ylabel("Force (N)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()1