import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_heatmap(data):
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()

def plot_outliers(data, column):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=data[column])
    plt.title(f'Outliers in {column}')
    plt.show()

def plot_histogram(data, column, bins=20):
    plt.figure(figsize=(10, 6))
    plt.hist(data[column], bins=bins, edgecolor='k')
    plt.title(f'{column} Distribution')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()
