
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random
import os

# Load the provided CSV file
csv_file = 'sales_data.csv'
try:
    df = pd.read_csv(csv_file)
    print(f"Dataset loaded from {csv_file}")
except FileNotFoundError:
    print(f"Error: {csv_file} not found.")
    exit(1)

# Convert Date to datetime and extract Month for analysis
try:
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y', errors='raise')
except ValueError as e:
    print(f"Error parsing dates: {e}")
    print("Attempting to parse with mixed format as fallback...")
    df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True)
df['Month'] = df['Date'].dt.strftime('%B')

# Statistical calculations using NumPy
def print_stats(data, column):
    print(f"\nStatistics for {column}:")
    print(f"Mean: ${np.mean(data):.2f}")
    print(f"Median: ${np.median(data):.2f}")
    print(f"Std Dev: ${np.std(data):.2f}")
    print(f"Min: ${np.min(data):.2f}")
    print(f"Max: ${np.max(data):.2f}")

print_stats(df['Total_Sales'], 'Total Sales')

# User interaction for month selection
months = df['Month'].unique()
print("\nAvailable months:", ", ".join(months))
selected_month = input("Enter a month to analyze (or 'all' for all months): ").capitalize()

if selected_month != 'All' and selected_month not in months:
    print(f"Invalid month. Analyzing all months.")
    selected_month = 'All'

# Filter data based on selected month
if selected_month != 'All':
    filtered_df = df[df['Month'] == selected_month]
else:
    filtered_df = df

# Visualization 1: Total Sales by Product Category
plt.figure(figsize=(10, 6))
category_sales = filtered_df.groupby('Product_Category')['Total_Sales'].sum()
category_sales.plot(kind='bar', color='skyblue')
plt.title(f'Total Sales by Product Category ({selected_month})')
plt.xlabel('Product Category')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_by_category.png')
plt.show()

# Visualization 2: Units Sold Distribution
plt.figure(figsize=(10, 6))
plt.hist(filtered_df['Units_Sold'], bins=20, color='lightgreen', edgecolor='black')
plt.title(f'Units Sold Distribution ({selected_month})')
plt.xlabel('Units Sold')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('units_sold_distribution.png')
plt.show()

# Visualization 3: Total Sales Trend Over Time
plt.figure(figsize=(10, 6))
monthly_sales = filtered_df.groupby(filtered_df['Date'].dt.to_period('M'))['Total_Sales'].sum()
monthly_sales.plot(kind='line', marker='o', color='coral')
plt.title(f'Monthly Sales Trend ({selected_month})')
plt.xlabel('Month')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_sales_trend.png')
plt.show()

# Visualization 4: Price per Unit vs Units Sold Scatter
plt.figure(figsize=(10, 6))
plt.scatter(filtered_df['Price_per_Unit'], filtered_df['Units_Sold'], alpha=0.5, color='purple')
plt.title(f'Price per Unit vs Units Sold ({selected_month})')
plt.xlabel('Price per Unit ($)')
plt.ylabel('Units Sold')
plt.tight_layout()
plt.savefig('price_vs_units.png')
plt.show()

# Print summary for selected month
print(f"\nSummary for {selected_month}:")
print(f"Total Sales: ${filtered_df['Total_Sales'].sum():.2f}")
print(f"Average Units Sold per Transaction: {filtered_df['Units_Sold'].mean():.2f}")
print(f"Average Price per Unit: ${filtered_df['Price_per_Unit'].mean():.2f}")