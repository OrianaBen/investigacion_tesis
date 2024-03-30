import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def calculate_hurst(data):
    """
    Calculate the Hurst exponent (H) using the R/S analysis method.
    :param data: 2D data (e.g., gravity measurements)
    :return: Hurst exponent (H)
    """
    n = len(data)
    cumsum = np.cumsum(data - np.mean(data))
    rs = np.max(cumsum) - np.min(cumsum)
    std_dev = np.std(data)
    hurst_exponent = np.log(rs / std_dev) / np.log(n)
    return hurst_exponent

# Generate or load your 2D data (replace with your actual data)
# For demonstration purposes, let's create a random walk series
df = pd.read_csv('anomalia_airelibre_5arcmin.csv', index_col=False)
data_2d = df.iloc[:,2]

# Calculate the Hurst exponent
hurst_value = calculate_hurst(data_2d)

# Print the result
print(f"Hurst exponent (H) = {hurst_value:.4f}")
