import numpy as np # Importing numpy for numerical operations

import matplotlib.pyplot as plt # Importing matplotlib for data visualization


import statistics # Importing statistics for mean, median, and mode calculations

# Function to calculate mean, median, and mode

import seaborn as sns # Importing seaborn for dataset loading and visualization
df = sns.load_dataset("tips") # Load the tips dataset from seaborn
print(df.head()) # Display the first few rows of the dataset

np.mean(df["total_bill"]) # Calculate the mean of the total bill column
print("Mean of total_bill:", np.mean(df["total_bill"])) # Print the mean

np.median(df["total_bill"])
print("Median of total_bill:", np.median(df["total_bill"]))

statistics.mode(df["total_bill"]) # Calculate the mode of the total bill column
print("Mode of total_bill:", statistics.mode(df["total_bill"])) # Print the mode




