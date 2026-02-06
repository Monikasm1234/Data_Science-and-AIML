contacts = {
    "Alice": "9876543210",
    "Bob": "9123456789",
    "Charlie": "9988776655"
}

contacts["Diana"] = "9012345678"

contacts["Bob"] = "9000000000"

existing_contact = contacts.get("Alice", "Contact not found")
missing_contact = contacts.get("Eve", "Contact not found")

print("Safe Lookup Results:")
print("Alice:", existing_contact)
print("Eve:", missing_contact)

print("Contact List:")

for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
