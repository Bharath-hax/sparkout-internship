
def student_dict():
    contacts = {}

    name = input("Enter your name: ")
    phone = input("Enter phone number: ")

    contacts[name]=phone

    print("\nContacts:")
    for key, value in contacts.items():
        print(key,value)

    return contacts


def check_contact(contacts):
    d_name = input("\nEnter the name to search: ")

    if d_name in contacts:
        print(f"The phone number of {d_name} is {contacts[d_name]}")
    else:
        print(f"{d_name} is not found")


contacts = student_dict()
check_contact(contacts)

def search_phone(contacts):
     d_phone = input("\nEnter the phone number to search: ")

     for name,phone in contacts.items():
         if phone==d_phone:
            print(f"The phone number of {d_phone} is {name}")
         else:
            print(f"{d_phone} is not found ")
contacts=student_dict()
search_phone(contacts)

def update_contact(contacts):
    u_name=input("enter the contact name ")
    if u_name in contacts:
        new_phone=input("enter the new contact number")
        contacts[u_name]=new_phone
        print("contact updated succesfully!")
        print(f"{u_name}:{contacts[u_name]}")
    else:
         print(f"{u_name} is not found!")
         
contacts=student_dict()
update_contact(contacts)

def delete_acount(contacts):
    r_name=input("enter the name u want to remove:")
    if r_name in contacts:
        del contacts[r_name]
        print("the contact deleted sucessfully!")

    else:
        print(f"{r_name} not found")
        
contacts=student_dict()
delete_acount(contacts)


    
