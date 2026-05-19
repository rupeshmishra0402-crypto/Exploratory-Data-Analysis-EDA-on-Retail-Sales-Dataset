import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("sales.csv")

# Data info
print(df.head())
print(df.info())

# Convert date
df['Date'] = pd.to_datetime(df['Date'])

# Analysis
print("Total Sales:", df['Sales'].sum())

region_sales = df.groupby('Region')['Sales'].sum()
print(region_sales)

# Visualization
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.show()

sns.histplot(df['Profit'], kde=True)
plt.show()
