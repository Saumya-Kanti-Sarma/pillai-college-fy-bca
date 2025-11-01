"""
Dictionary-Based Application 
Build a phonebook application. 
● Add new contacts to the dictionary. 
● Search for a contact by name. 
● Update an existing contact’s number. 
● Delete a contact. 
● Display all contacts in alphabetical order of names.
"""
contact = {
    "Abi":987654320,
    "Roshan":789456120,
    "Saumya":12457890
}
print("All contacts:",contact)

# Add new contacts to the dictionary
print("Add to Contact")
name = input("Enter Name : ")
ph = int(input("Enter number : "))
contact.update({name:ph})
print(contact)

# Search for a contact by name
inp = input("Search Contact: ")
data = contact.get(inp)
print(inp, ":",data)

# Update an existing contact’s number. 
name = input("Update Contact: ")
is_available = contact.get(name)
if is_available == False:
    print("No contact available")
else:
    ph = int(input("Enter number : "))
    contact.update({name:ph})
    print(contact)

#Delete a contact. 
name = input("Delete Contact: ")
is_available = contact.get(name)
if is_available== None:
    print("No contact available")
else:
    del contact[name]
    print(contact)

# print dictionary in sorted order:
for name in sorted(contact.keys()):
    print(f"{name}: {contact[name]}")
