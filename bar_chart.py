import matplotlib.pyplot as plt
products = ["Laptop","Mobile","Tablet","Monitor"]
sales = [50,80,30,60]

plt.bar(products, sales)

plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Sales per Products")
plt.show()