
import seaborn as sns  # Import seaborn before using sns
import matplotlib.pyplot as plt  # Import matplotlib before using plt

df = sns.load_dataset("tips")  # Define df before using it
sns.boxplot(x = df["total_bill"]) # Create a boxplot for the total bill column
print("Boxplot of total_bill:") # Print statement for clarity
import matplotlib.pyplot as plt # Importing matplotlib for plotting

plt.show() # Show the boxplot
plt.savefig("boxplot.png")  # Saves the figure to a file