# aml_monitor.py - Simple AML Monitoring Prototype
# Magdalene Madike - January 2026

print("=== AML Monitoring Dashboard Prototype ===")
print("Author: Magdalene Madike")
print("Processing 100 sample transactions...\n")

# Mock results (we'll make it smarter later)
high_risk = 7
medium_risk = 18
low_risk = 75

print(f"Transactions processed: 100")
print(f"High Risk (recommend STR): {high_risk}")
print(f"Medium Risk (review): {medium_risk}")
print(f"Low Risk: {low_risk}")

print("\nExample high-risk transaction:")
print("TXN_017 | Risk Score: 92 | Flags: structuring + sanctioned country + velocity spike")
print("\nDone! Results saved to aml_monitoring_results.csv (coming soon)")
