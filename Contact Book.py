print("Welcome to the Contact Book")
print("1. Add a contact\n"
      "2. Search a contact\n"
      "3. Display contacts\n"
      "4. Edit a contact\n"
      "5. Delete a contact\n"
      "6. Exit\n")
Contact = {}
while True:
    a = input("What do you want to do?(Choose Between 1-6)").strip()
    if a == "1":
        Add_name = input("Type the name: ")
        Add_num = input("Type the number: ")
        Contact[Add_name] = Add_num
        print("Contact Number Added Successfully")
        print(f"Name: {Add_name}\nNumber: {Add_num}")
    elif a == "2":
        Search_contact = input("Type the name you want to find: ")
        if Search_contact in Contact:
            print(f"Here's the contact:\nName: {Search_contact}\nNumber: {Contact[Search_contact]}")
        else:
            print("Contact not found")
    elif a == "3":
        print("The contacts are:")
        for name, number in Contact.items():
            print(f"Name: {name}, Numbers: {number}")
        # print(Contact.items())
    elif a == "4":
        Edit_contact = input("Type the name of the contact to edit:")
        # Updated_num = input("Edit the number: ")
        if Edit_contact in Contact:
            print("Yes, the contact exists")
            Updated_num = input("Edit the number: ")
            Contact[Edit_contact]=Updated_num
            print("Contact has been edited successfully")
            # print(Contact[Edit_contact])
            #only to display the particular contact
            #edit the name also
        else:
            print("Contact not found")
    elif a == "5":
        del_contact = input("Type the name to delete the contact: ")
        if del_contact in Contact:
            del Contact[del_contact]
            print(f"{del_contact} has been deleted.")
        else:
            print("Contact not found")
    elif a =="6":
        break
