import pandas as pd

# Create Series with custom labels
products = pd.Series(
    [700, 150, 300],
    index=["Laptop", "Mouse", "Keyboard"]
)

# Access Laptop price using label-based indexing
laptop_price = products["Laptop"]

# Slice first two products using positional indexing
first_two = products.iloc[0:2]

# Output
print("Full Product Series:\n")
print(products)

print("\nPrice of Laptop:")
print(laptop_price)

print("\nFirst Two Products (Positional Slicing):")
print(first_two)
