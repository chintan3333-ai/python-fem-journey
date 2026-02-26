# ===================================
# Stress Calculator v2.0
# By Chintan
# Features: Multiple materials,
#           Plot, File save
# ===================================

import matplotlib.pyplot as plt

# Material yield strengths (MPa)
materials = {
    "1": ("Mild Steel",    250),
    "2": ("Aluminum",      270),
    "3": ("Titanium",      880),
    "4": ("Cast Iron",     200),
}

# Display material menu
print("=== STRESS CALCULATOR v2.0 ===\n")
print("Select Material:")
for key, (name, strength) in materials.items():
    print(f"  {key}. {name} (Yield: {strength} MPa)")

choice = input("\nEnter choice (1-4): ")
material_name, yield_strength = materials[choice]

# Input values
force = float(input("Enter applied force (N): "))
area  = float(input("Enter cross-sectional area (mm²): "))

# Calculate stress
stress = force / area
safety_factor = yield_strength / stress

# Display results
print(f"\n--- RESULTS ---")
print(f"Material        : {material_name}")
print(f"Applied Force   : {force} N")
print(f"Cross-section   : {area} mm²")
print(f"Stress          : {stress:.2f} MPa")
print(f"Yield Strength  : {yield_strength} MPa")
print(f"Safety Factor   : {safety_factor:.2f}")

if stress > yield_strength:
    status = "3 FAILED: Stress exceeds yield strength!"
elif stress > 0.8 * yield_strength:
    status = " WARNING: Approaching yield strength!"
elif stress > 0.5 * yield_strength:
    status = "  CAUTION: Moderate stress level."
else:
    status = " SAFE: Within acceptable limits."

print(f"Status          : {status}")

# Save results to file
with open("stress_results.txt", "w") as f:
    f.write("=== STRESS CALCULATOR RESULTS ===\n")
    f.write(f"Material        : {material_name}\n")
    f.write(f"Applied Force   : {force} N\n")
    f.write(f"Cross-section   : {area} mm²\n")
    f.write(f"Stress          : {stress:.2f} MPa\n")
    f.write(f"Yield Strength  : {yield_strength} MPa\n")
    f.write(f"Safety Factor   : {safety_factor:.2f}\n")
    f.write(f"Status          : {status}\n")

print("\n✅ Results saved to stress_results.txt")

# Plot stress vs force
forces = [i * 1000 for i in range(1, 21)]
stresses = [f / area for f in forces]

plt.figure(figsize=(8, 5))
plt.plot(forces, stresses, color='blue', linewidth=2, label='Stress')
plt.axhline(y=yield_strength, color='red', linestyle='--',
            linewidth=2, label=f'Yield Strength ({yield_strength} MPa)')
plt.axhline(y=stress, color='green', linestyle='-.',
            linewidth=1.5, label=f'Your Stress ({stress:.1f} MPa)')
plt.title(f"Stress vs Force — {material_name}")
plt.xlabel("Force (N)")
plt.ylabel("Stress (MPa)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()