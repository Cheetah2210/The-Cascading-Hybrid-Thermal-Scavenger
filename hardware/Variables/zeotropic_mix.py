# variables/zeotropic_mix.py

def evaluate_zeotropic_blend(refrigerant_a, refrigerant_b, ratio_a):
    """
    Models temperature glide and heat exchanger optimization 
    for binary zeotropic working fluids in the scavenger loops.
    """
    ratio_b = 1.0 - ratio_a
    print(f"--- Zeotropic Blend Optimization Profile ---")
    print(f"Mixture Composition: {refrigerant_a} ({ratio_a*100:.0f}%) / {refrigerant_b} ({ratio_b*100:.0f}%)")
    
    # Standard pure fluids have 0°C glide (boil at a single flat temperature)
    # Zeotropic mixtures experience a temperature glide during phase change
    if refrigerant_a == "R-290" and refrigerant_b == "R-600a":
        # Approximate temperature glide range based on standard mixtures
        temperature_glide_c = 7.4 * (1.0 - abs(ratio_a - 0.6) * 2.0)
        exergy_efficiency = 0.70 + (0.16 * (temperature_glide_c / 7.4))
    else:
        temperature_glide_c = 2.0
        exergy_efficiency = 0.72
        
    print(f" -> Phase Change Temperature Glide: {temperature_glide_c:.2f}°C")
    print(f" -> Heat Exchanger Exergy Efficiency: {exergy_efficiency*100:.1f}%")
    
    # Calculate performance delta against baseline pure R-134a (Fixed point)
    pure_baseline_eff = 0.70
    performance_boost = ((exergy_efficiency - pure_baseline_eff) / pure_baseline_eff) * 100
    print(f" -> Net Thermal Performance vs Pure Baseline: +{performance_boost:.1f}% Efficiency Gain")

if __name__ == "__main__":
    # Test the optimal 60/40 Propane-Isobutane variable profile
    evaluate_zeotropic_blend("R-290", "R-600a", 0.60)
