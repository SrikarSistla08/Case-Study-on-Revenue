import pandas as pd
import random
import datetime

# Sample Data Generation
num_rows = 1000
data = {
    "Customer_ID": [f"C{str(random.randint(1, 100)).zfill(3)}" for _ in range(num_rows)],
    "Order_ID": [f"O{str(random.randint(10000, 99999))}" for _ in range(num_rows)],
    "Date": [datetime.date(2023, random.randint(1, 12), random.randint(1, 28)) for _ in range(num_rows)],
    "Product_Category": random.choices(["Electronics", "Fashion", "Home & Kitchen", "Sports"], k=num_rows),
    "Revenue": [round(random.uniform(20, 500), 2) for _ in range(num_rows)],
    "Cost": [round(random.uniform(10, 300), 2) for _ in range(num_rows)],
    "Region": random.choices(["North", "South", "East", "West"], k=num_rows),
    "Age": [random.randint(18, 65) for _ in range(num_rows)],
    "Income": [round(random.uniform(30000, 100000), 2) for _ in range(num_rows)],
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("Customer_Data.csv", index=False)
print("Customer_Data.csv created successfully!")
