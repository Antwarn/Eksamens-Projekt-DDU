import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV
data = pd.read_csv("google26.csv")

# Convert 'Time' column to datetime
data['Time'] = pd.to_datetime(data['Time'])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(data['Time'], data['Last'], label='Last Price', color='green')
plt.title('Stock Close Price Over Time')
plt.xlabel('Time')
plt.ylabel('Close Price')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
