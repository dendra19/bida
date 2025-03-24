import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load the CSV file into a DataFrame
file_path = 'C:\WineQT.csv'
df = pd.read_csv(file_path)
#df = pd.read.csv(file_path)

#Summary statistics
summary_stats = df.describe()
print("Summary Statistics")
print(summary_stats)

#Correlation matrix
correlation_matrix = df.corr()
print("\nCorrelation Matrix: ")
print(correlation_matrix)

#Quality distribution
quality_distribution = df['quality'].value_counts().sort_index()
print("\nQuality Distribution: ")
print(quality_distribution)

#Correlation with quality
quality_correlation = correlation_matrix['quality'].sort_values(ascending=False)
print("\nQuality Correlation: ")
print(quality_correlation)

# Correlation with quality
quality_correlation = correlation_matrix ['quality'].sort_values (ascending=False) 
print("\nCorrelation with Quality:")
print (quality_correlation)

#Plotting
plt.figure (figsize=(10, 6))

#Quality distribution plot
plt.subplot (2, 2, 1)
sns.countplot (x='quality', data=df, palette='viridis')
plt.title('Quality Distribution')

#Heatmap of correlation matrix
plt.subplot(2, 2, 2)
sns.heatmap (correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix Heatmap')

#Alcohol vs Quality
plt.subplot (2, 2, 3)
sns.boxplot (x='quality', y='alcohol', data=df, palette='viridis')
plt.title('Alcohol vs Quality')

#Density vs Quality
plt.subplot (2, 2, 4)
sns.boxplot (x='quality', y='density', data=df, palette='viridis')
plt.title('Density vs Quality')
plt.tight_layout ()
plt.show()
