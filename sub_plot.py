import matplotlib.pyplot as plt

x = [1,2,3,4]
y1 = [10,20,25,30]
y2 = [30,25,20,15]

plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.plot(x,y1)
plt.title("Increasing Trend")

plt.subplot(1,2,2)
plt.plot(x,y2)
plt.title("Decreasing Trend")

plt.tight_layout()
plt.show()
