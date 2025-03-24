import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the CSV data into a pandas DataFrame
def load_data(csv_file):
    try:
        data = pd.read_csv('C:\sales_data.csv', encoding="ISO-8859-1")
        print("Data loaded successfully!")
        print(data)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Step 2: Perform basic data inspection
def data_summary(data):
    print("\nFirst 5 rows of the data:")
    print(data.head())  # Displays the first 5 rows
    
    print("\nData Structure:")
    print(data.info())  # Get information on the DataFrame such as column types and non-null counts
    
    print("\nStatistical summary of numeric columns:")
    print(data.describe())  # Gives summary statistics for numeric columns

# Step 3: Visualize the data

# Visualization 1: Total Sales Over Time
def plot_sales_over_time(data):
    # Convert 'Date' to datetime if it's not already in the correct format
    data['Date'] = pd.to_datetime(data['Date'])
    
    # Aggregate data by Date and calculate the total sales for each day
    sales_by_date = data.groupby('Date')['Sales_Amount'].sum().reset_index()
    
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Date', y='Sales_Amount', data=sales_by_date, marker='o')
    plt.title('Total Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Sales ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Visualization 2: Sales Distribution by Region
def plot_sales_by_region(data):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Region', y='Sales_Amount', data=data)
    plt.title('Sales Distribution by Region')
    plt.xlabel('Region')
    plt.ylabel('Sales Amount ($)')
    plt.tight_layout()
    plt.show()

# Visualization 3: Sales vs Quantity Sold (Scatter Plot)
def plot_sales_vs_quantity(data):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Quantity_Sold', y='Sales_Amount', data=data, hue='Product', palette='viridis')
    plt.title('Sales Amount vs Quantity Sold')
    plt.xlabel('Quantity Sold')
    plt.ylabel('Sales Amount ($)')
    plt.tight_layout()
    plt.show()

# Visualization 4: Top Products by Sales
def plot_top_products_by_sales(data):
    top_products = data.groupby('Product')['Sales_Amount'].sum().reset_index()
    top_products = top_products.sort_values('Sales_Amount', ascending=False).head(10)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Sales_Amount', y='Product', data=top_products, palette='Blues_d')
    plt.title('Top 10 Products by Sales Amount')
    plt.xlabel('Sales Amount ($)')
    plt.ylabel('Product')
    plt.tight_layout()
    plt.show()

# Main function to load data and generate visualizations
def main():
    csv_file = 'sales_data.csv'  # Replace with your actual CSV file path
    data = load_data(csv_file)
    
    if data is not None:
        # Step 2: Data summary and inspection
        data_summary(data)

        # Step 3: Data Visualizations
        plot_sales_over_time(data)
        plot_sales_by_region(data)
        plot_sales_vs_quantity(data)
        plot_top_products_by_sales(data)

# Entry point of the program
if __name__ == "__main__":
    main()
