import seaborn as sns  # Import seaborn for data visualization
import matplotlib.pyplot as plt  # Import matplotlib for plotting
import numpy as np  # Import numpy for numerical operations

df1 = sns.load_dataset("iris")  # Load the iris dataset

percentiles = np.percentile(df1["sepal_length"], [25, 75, 90])  # Calculate percentiles
print("Percentile:", percentiles)  # Print the calculated percentiles
