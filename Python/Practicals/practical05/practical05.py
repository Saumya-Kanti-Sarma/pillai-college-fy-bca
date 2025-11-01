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
    "Tvisha":987654320,
    "Roshan":789456120,
    "Saumya":12457890
}

name = input("Enter name : ")
ph = int(input("Enter number : "))
contact.update({name:ph})
print(contact)

inp = input("Enter name to search: ")
data = contact.get(inp)
print(inp, ":",data)

name = input("Enter name : ")
is_available = contact.get(name)

if is_available == False:
    print("No contact available")
else:
    ph = int(input("Enter number : "))
    contact.update({name:ph})
    print(contact)


name = input("Enter name : ")
is_available = contact.get(name)
if is_available== None:
    print("No contact available")
else:
    del contact[name]
    print(contact)

while True:
    task = input("Enter 'a' to add new contact, 's' to search, 'd' to delete and 'c' to show all contact: ")
    task.lower()
    if task == "a":
        #Add new contacts to the dictionary. 
        name = input("Enter name : ")
        ph = int(input("Enter number : "))
        contact.update({name:ph})
        print(contact)
    elif task == "s":
        #Search for a contact by name. 
        inp = input("Enter name to search: ")
        data = contact.get(inp)
        print(inp, ":",data)
    elif task == "u":
        #Update an existing contact’s number.
        name = input("Enter name : ")
        is_available = contact.get(name)

        if is_available == None:
            print("No contact available")
        else:
            ph = int(input("Enter number : "))
            contact.update({name:ph})
            print(contact)
    elif task == "d":
        #Delete a contact.
        name = input("Enter name : ")
        is_available = contact.get(name)

        if is_available== None:
            print("No contact available")
        else:
            del contact[name]
            print(contact)
    elif task == "c":
        if contact:
            print("All contacts (sorted by name):")
            for name in sorted(contact.keys()):
                print(f"{name}: {contact[name]}")
        else:
            print("No contacts available")
    elif task =="break":
        break

