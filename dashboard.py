import matplotlib.pyplot as plt

# ----- Bar Chart Data -----
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

# ----- Line Plot Data (example trend) -----
months = [1, 2, 3, 4, 5]
trend_sales = [200, 250, 300, 280, 350]

# Create figure

# Subplot 1 → Bar Chart
plt.subplot(1, 2, 1)
plt.bar(categories, sales, color='skyblue')
plt.title("Sales by Category")
plt.xlabel("Categories")
plt.ylabel("Sales")

# Subplot 2 → Line Plot
plt.subplot(1, 2, 2)
plt.plot(months, trend_sales, marker='o')
plt.title("Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

# Prevent overlapping
plt.tight_layout()

# Display plots
plt.show()
