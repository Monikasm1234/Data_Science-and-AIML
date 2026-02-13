import matplotlib.pyplot as plt

# Data
months = [1, 2, 3, 4, 5]
revenue = [2000, 4500, 4000, 7500, 9000]

# Create Line Plot
plt.plot(months, revenue)

# Add Title and Labels
plt.title("Monthly Revenue Growth")
plt.xlabel("Month")
plt.ylabel("Revenue in USD")

# Display the Plot
plt.show()
