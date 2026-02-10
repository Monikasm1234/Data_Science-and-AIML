file = open("sample.txt","w")
file.write("Hello, this is a file handling example.")
file.close()

file = open("samp.txt","w")
file.write("Hello.")
file.close()

file = open("sample.txt","r")
content = file.read()
print(content)
file.close()

with open("sample.txt","r") as file:
    content = file.read()
    print(content)

with open("sample.txt","a") as file:
    file.write("\nsecond data added\n")

with open("sample.txt","a") as file:
    file.write("\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n")

with open("sample.txt","r") as file:
    for line in file:
        print(line.strip())
        