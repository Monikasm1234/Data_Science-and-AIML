#list Methods
fruits = ["Apples", "Bananas", "Carrots", "Dates"]
print(fruits)

fruits.append("Eggs")
print(fruits)

fruits.remove("Bananas")
print(fruits)

fruits.sort()
print(fruits)


#indexing and slicing
temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]

print(temperatures[0])
print(temperatures[-1])

print(temperatures[3:6])

print(temperatures[-3])


# Tuples
screen_res = (1920, 1080)
print("Current Resolution:", screen_res)

#screen_res[0] = 1280

print("Tupes cannot be modified")