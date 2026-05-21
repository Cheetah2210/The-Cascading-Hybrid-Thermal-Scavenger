import csv
import time
from datetime import datetime

def log_system_data(voltage, temp_in, temp_out):
    # Calculate power proxy locally
    # P = V^2 / R (using 0.02 Ohm proxy)
    resistance = 0.02
    volts = voltage / 1000.0
    power_mw = ((volts ** 2) / resistance) * 1000.0
    
    # Get current timestamp
    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    
    # Create or append to the CSV file
    file_name = "simulations/chts_live_data.csv"
    
    with open(file_name, "a", newline="") as f:
        writer = csv.writer(f)
        
        # Write row data
        writer.writerow([
            current_time,
            f"{temp_in:.1f}",
            f"{temp_out:.1f}",
            f"{voltage:.1f}",
            f"{power_mw:.2f}"
        ])

if __name__ == "__main__":
    # Test a single logging entry
    # (55C exhaust, 24C ambient, 15mV output)
    log_system_data(
        voltage=15.0, 
        temp_in=55.0, 
        temp_out=24.0
    )
    print("Data logged locally to CSV successfully.")
