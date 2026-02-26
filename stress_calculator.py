# ===================================
# Simple Stress Calculator
# By Chintan
# ===================================

# Input values
force = float(input("Enter applied force (N): "))
area = float(input("Enter cross-sectional area (mm²): "))

# Calculate stress
stress = force / area

# Display result
print(f"\n--- RESULTS ---")
print(f"Applied Force   : {force} N")
print(f"Cross-section   : {area} mm²")
print(f"Stress          : {stress:.2f} MPa")

# Safety check
if stress > 250:
    print("⚠️  WARNING: Stress exceeds yield strength of mild steel!")
elif stress > 150:
    print("⚠️  CAUTION: Approaching yield strength!")
else:
    print("✅  SAFE: Within acceptable stress limits.")