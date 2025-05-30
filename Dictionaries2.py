#

contacts = {
    "Alice": "123-456-7890",   
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555",
    "Dave": "444-444-4444",
    "Eve": "222-222-2222"
    }

print("Number of contacts:", len(contacts))
print("Contacts:")
for contact, number in contacts.items():
    print("The number for {contact} is {number}.".format(contact=contact, number=number))

print('Eve' in contacts.keys())    