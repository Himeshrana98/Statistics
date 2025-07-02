
import seaborn as sns  # Import seaborn for data visualization
import matplotlib.pyplot as plt  # Import matplotlib for plotting       


df1 = sns.load_dataset("iris")  # Load the Iris dataset from seaborn
print(df1.head())  # Display the first few rows of the dataset
sns.countplot(x = df1["species"])  # Create a count plot for the species column
plt.title("Count Plot of Species")  # Set the title for the count plot
plt.xlabel("Species")  # Set the x-axis label
plt.ylabel("Count")  # Set the y-axis label
sns.countplot(x=df1["species"], palette=["red", "green", "blue"])  # Create a count plot with custom colors for each species
plt.show()  # Show the count plot
plt.savefig("count_plot_species.png")  # Saves the count plot to a file
# Compare this snippet from bar_graph.py: