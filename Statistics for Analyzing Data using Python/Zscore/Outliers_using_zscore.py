#Detect_Outliers_using_zscore

import numpy as np   # Numerical operations
import matplotlib.pyplot as plt   # Data visualization
# This code detects outliers in a dataset using the Z-score method.

# Sample data
dataset = [11, 10, 12, 14, 12, 15, 14, 13, 15, 102, 12, 14, 17, 19, 107, 10, 13, 12, 14, 12, 108, 12, 11] # Example data with an outlier (102, 107, 108)

plt.hist(dataset)

# ZSCORE METHOD

outliers = [] # List to hold outliers
# Function to detect outliers using Z-score method
def detect_outliers(data):
    # Calculate the Z-scores of the data
    threshold = 2 # 2 standard deviations
    mean = np.mean(data) # Mean of the data
    std = np.std(data)
    
    for i in data:
        z_score = (i-mean)/std # Z-score calculation
        if np.abs(z_score) > threshold:  # here abs function is used to get the absolute value of z_score  
            outliers.append(i) # If Z-score is greater than threshold, it is an outlier

    return outliers 
# Detect outliers in the dataset
outliers = detect_outliers(data =dataset)
# Output the detected outliers 
print("Outliers in the dataset:", outliers) 
