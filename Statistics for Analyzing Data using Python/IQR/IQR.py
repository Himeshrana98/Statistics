#IQR

#Steps to calculate IQR:
# 1. Sort the data in ascending order.
# 2. Find the first quartile (Q1) and third quartile (Q3).
# 3. Calculate the interquartile range (IQR) as IQR = Q3 - Q1.
# 4. Find the Lower fence (LF) as Q1 - 1.5 * IQR.
# 5. Find the Upper fence (UF) as Q3 + 1.5 * IQR. 

dataset = [11, 10, 12, 14, 12, 15, 14, 13, 15, 102, 12, 14, 17, 19, 107, 10, 13, 12, 14, 12, 108, 12, 11]  # Example data
dataset = sorted(dataset)  # an inbuilt function to sort the dataset
print(dataset)

# Calculate the first quartile (Q1) and third quartile (Q3)
# The first quartile (Q1) is the median of the first half of the data   
# The third quartile (Q3) is the median of the second half of the data

Q1 = dataset[len(dataset) // 4]  # 25% percentile
Q3 = dataset[len(dataset) * 3 // 4] # 75% percentile

print("Q1,Q3:", Q1, Q3) # Q1,Q3: 12 15

# Calculate the interquartile range (IQR)

IQR = Q3 - Q1
print("IQR:", IQR) # IQR IS 3

# Calculate the lower and upper fences
lower_fence = Q1 - (1.5 * IQR)
upper_fence = Q3 + (1.5 * IQR)
print("Lower Fence:", lower_fence)  # Lower Fence: 6.5
print("Upper Fence:", upper_fence)  # Upper Fence: 20.5
# Identify outliers
outliers = [x for x in dataset if x < lower_fence or x > upper_fence]
print("Outliers:", outliers)  # Outliers: [102, 107, 108]

import seaborn as sns # seaborn is a data visualization library based on matplotlib
sns.boxplot(x = dataset) # boxplot is a method in seaborn to visualize the distribution of the dataset
print("Boxplot created") # This will print a message indicating that the boxplot has been created
import matplotlib.pyplot as plt # Importing matplotlib for plotting

plt.show() # Show the boxplot
plt.savefig("boxplot.png")  # Saves the figure to a file
