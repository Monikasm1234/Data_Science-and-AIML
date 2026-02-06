total_bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))

share_per_person = total_bill / people

print("Total Bill:", total_bill, ". \nEach person pays:", share_per_person)

print(type(total_bill))
print(type(people))
print(type(share_per_person))
