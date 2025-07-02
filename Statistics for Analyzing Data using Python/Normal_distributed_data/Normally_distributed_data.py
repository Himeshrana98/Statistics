
import seaborn as sns  # Import seaborn for data visualization
import matplotlib.pyplot as plt  # Import matplotlib for plotting
import numpy as np  # Import numpy for numerical operations
import statistics  # Import statistics for mean, median, and mode calculations
import scipy.stats as stats  # Import scipy for statistical functions

df1 = sns.load_dataset("iris")  # Load the Iris dataset from seaborn
print(df1.head())  # Display the first few rows of the dataset

sns.histplot(x = df1["sepal_length"], kde = True) # Create a histogram with KDE for the total bill column
plt.title("Histogram of Total Bill") # Set the title for the histogram
plt.xlabel("Total Bill") # Set the x-axis label
plt.ylabel("Count") # Set the y-axis label
plt.show() # Show the histogram
plt.savefig("histogram.png")  # Saves the histogram to a file