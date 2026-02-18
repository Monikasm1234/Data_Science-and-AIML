import random

trials = 100000

# ---------- Independent Events ----------
independent_success = 0

for _ in range(trials):
    coin = random.choice(["H", "T"])
    die = random.randint(1, 6)

    if coin == "H" and die == 6:
        independent_success += 1

independent_probability = independent_success / trials

print("Independent Event Probability (H and 6):")
print(independent_probability)


# ---------- Dependent Events (Marbles) ----------
dependent_success = 0

for _ in range(trials):
    bag = ["R"] * 5 + ["B"] * 5

    first = random.choice(bag)
    bag.remove(first)     # WITHOUT replacement

    second = random.choice(bag)

    if first == "R" and second == "R":
        dependent_success += 1

dependent_probability = dependent_success / trials

print("\nDependent Event Probability (Both Red):")
print(dependent_probability)
