import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')

# Data Cleaning and Preparation
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

df["price"] = (
    pd.to_numeric(
        df["price"].astype(str).str.replace(",", ""),
        errors="coerce"
    )
    .astype(float)
)

df["area"] = pd.to_numeric(df["area"], errors="coerce")
df["rate_per_sqft"] = (
    pd.to_numeric(
        df["rate_per_sqft"].astype(str).str.replace(",", ""),
        errors="coerce"
    )
)

df["status"] = df["status"].str.strip().str.lower()
df["rera_approval"] = df["rera_approval"].str.strip().str.lower()
df["flat_type"] = df["flat_type"].str.strip().str.lower()

df = df.drop_duplicates()

# Question 1: Which is the costliest flat?
cost_flat=df.loc[df["price"].idxmax()]
print(cost_flat)

# Question 2: Which locality has the highest average price?
highest_average_price=df.groupby("locality")["price"].mean().sort_values(ascending=False)
print( highest_average_price)

# Question 3: Which locality has the highest rate per square foot?
highest_rated=df.groupby("locality")["rate_per_sqft"].mean().sort_values(ascending=False)

# Question 4: Ready-to-move vs Under-construction pricing
df.groupby("status")["price"].median()

# Question 5: Does RERA approval affect pricing?
df.groupby("rera_approval")["price"].median()

# Question 6: How does area impact price?
sns.scatterplot(x="area", y="price", data=df)
plt.show()

# Question 7: Which BHK configuration is most expensive?
df.groupby("bhk_count")["price"].mean()

# Question 8: Which property type is the costliest?
df.groupby("flat_type")["price"].mean()

# Question 9: Do certain builders price higher?
df.groupby("company_name")["price"].mean().sort_values(ascending=False)

# Question 10: Are larger homes more expensive per sqft?
sns.scatterplot(x="area", y="rate_per_sqft", data=df)
plt.show()