import matplotlib.pyplot as plt

months = [1,2,3,4,5]

sales = [100,150,200,280,160]

plt.plot(months, sales, label="Sales")

plt.xlabel("Monthly Sales Report")
plt.ylabel("Month")
plt.title("Sales Amount")
plt.legend()
plt.grid(True)

plt.show()