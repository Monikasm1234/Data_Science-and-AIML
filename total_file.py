item_name = "Laptop"     # String
quantity = 4             # Integer
price = 2999.99           # Float
in_stock = True          # Boolean

print("Item:", item_name, ", Qty:", quantity, ", Price:", price, ", Available:", in_stock)

total_cost = quantity * price

print("Total Cost:", total_cost)

total_bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))

share_per_person = total_bill / people

print("Total Bill:", total_bill, ". \nEach person pays:", share_per_person)

print(type(total_bill))
print(type(people))
print(type(share_per_person))

name = input("Enter your name:")

age = int(input("Enter your age:"))

age = age + 4

print("Hey", name, ", you will be", age, "years old in 2030!")