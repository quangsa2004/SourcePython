import pandas as pd

# Create a dictionary with sample sales data
sales_data = {
    'Product_ID': ['P001', 'P002', 'P003', 'P001', 'P002'],
    'Transaction_Date': ['2023-01-01', '2023-01-03', '2023-01-05', '2023-01-08', '2023-01-10'],
    'Quantity_Sold': [100, 120, 90, 110, 130],
    'Unit_Price': [10.99, 12.99, 9.99, 11.99, 13.99],
    'Customer_ID': ['C001', 'C002', 'C003', 'C001', 'C002']
}

# Create a DataFrame from the dictionary
sales_df = pd.DataFrame(sales_data)

# Convert 'Transaction_Date' column to datetime format
sales_df['Transaction_Date'] = pd.to_datetime(sales_df['Transaction_Date'])

# Display the DataFrame
print(sales_df)


# Check for missing values
print(sales_df.isnull().sum())


#If the data is not clean
#Filling missing values with the mean
sales_df['quantity_sold'].fillna(sales_df['quantity_sold'].mean(), inplace=True)

#Removing duplicated records:
sales_df.drop_duplicates(inplace=True)
#Min-Max normalization
sales_df['quantity_sold'] = (sales_df['quantity_sold'] - sales_df['quantity_sold'].min()) / (sales_df['quantity_sold'].max() - sales_df['quantity_sold'].min())
#One-hot encoding for day of the week
sales_df = pd.get_dummies(sales_df, columns=['day_of_week'])
#Selecting relevant features
selected_features = ['quantity_sold', 'day_of_week_0', 'day_of_week_1', 'day_of_week_2', 'day_of_week_3']
sales_df = sales_df[selected_features]

# Feature engineering
sales_df['day_of_week'] = sales_df['timestamp'].dt.dayofweek
sales_df['month'] = sales_df['timestamp'].dt.month

# Preview the updated DataFrame
print(sales_df)