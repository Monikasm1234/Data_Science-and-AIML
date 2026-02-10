
name = input("Enter your name: ")
daily_goal = input("Enter your daily goal: ")

with open("journaling.txt", "w") as file:
    file.write(f"Name: {name}, Daily Goal: {daily_goal}\n")

print("Your goal has been saved!")
