
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.histplot(x = df["total_bill"], kde = True) # Create a histogram with KDE for the total bill column
plt.title("Histogram of Total Bill") # Set the title for the histogram
plt.xlabel("Total Bill") # Set the x-axis label
plt.ylabel("Count") # Set the y-axis label
plt.show() # Show the histogram
plt.savefig("histogram.png")  # Saves the histogram to a file