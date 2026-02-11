import pandas as pd

# Create Series
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

# Clean the usernames
cleaned = usernames.str.strip().str.lower()

# Check which names contain the letter 'a'
contains_a = cleaned.str.contains('a')

# Output
print("Cleaned Usernames:\n")
print(cleaned)

print("\nContains letter 'a':\n")
print(contains_a)
