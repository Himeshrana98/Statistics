# correlation

import seaborn as sns
import pandas as pd


df = sns.load_dataset("iris")
print(df.head())
#   sepal_length  sepal_width  petal_length  petal_width species
#0           5.1          3.5           1.4          0.2  setosa
#1           4.9          3.0           1.4          0.2  setosa
#2           4.7          3.2           1.3          0.2  setosa
#3           4.6          3.1           1.5          0.2  setosa
#4           5.0          3.6           1.4          0.2  setosa

# Create a scatter plot for Sepal Length vs Sepal Width
import matplotlib.pyplot as plt

# Display correlation matrix (numeric columns only)
numeric_df = df.select_dtypes(include='number')
print("Pearson correlation matrix:")
print(numeric_df.corr(method='pearson'))

print("\nSpearman correlation matrix:")
print(numeric_df.corr(method='spearman'))
#   sepal_length  sepal_width  petal_length  petal_widt
# Create a scatter plot for Sepal Length vs Sepal Width
plt.scatter(df['sepal_length'], df['sepal_width'])
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Sepal Length vs Sepal Width')
plt.show()

sns.pairplot(df, x_vars=['sepal_length', 'sepal_width'], y_vars=['petal_length', 'petal_width'], hue='species')
plt.show()
