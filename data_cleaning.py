with open("day7.txt", "r") as file:
    for line in file:
        if line.strip():
            cleaned_line = line.strip()
            print(cleaned_line.upper())
            print(cleaned_line.lower())